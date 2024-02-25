# This file is placed in the Public Domain.
#
# pylint: disable=C,R,W0105,W0212,W0613,W0718,E0402


"handler"


import inspect
import queue
import threading
import time
import _thread


from objx import Default, Object, Persist, spl


from .brokers import Broker
from .excepts import Error
from .threads import launch


class Command(Object):

    cmds = Object()

    @staticmethod
    def add(func):
        setattr(Command.cmds, func.__name__, func)


class Message(Default):

    def __init__(self):
        Default.__init__(self)
        self._ready  = threading.Event()
        self._thr    = None
        self.done    = False
        self.orig    = None
        self.result  = []
        self.txt     = ""
        self.type    = "event"

    def ready(self):
        self._ready.set()

    def reply(self, txt):
        self.result.append(txt)

    def show(self):
        bot = Broker.get(self.orig)
        for txt in self.result:
            bot.say(self.channel, txt)

    def wait(self):
        if self._thr:
            self._thr.join()
        self._ready.wait()
        return self.result


class Handler(Object):

    def __init__(self):
        Object.__init__(self)
        self.cbs      = Object()
        self.queue    = queue.Queue()
        self.stopped  = threading.Event()
        self.threaded = True
        Broker.add(self)

    def callback(self, evt):
        func = getattr(self.cbs, evt.type, None)
        if not func:
            evt.ready()
            return
        if self.threaded:
            evt._thr = launch(func, evt)
        else:
            func(evt)
            evt.ready()

    def loop(self):
        while not self.stopped.is_set():
            try:
                evt = self.poll()
                self.callback(evt)
            except (KeyboardInterrupt, EOFError):
                _thread.interrupt_main()

    def poll(self):
        return self.queue.get()

    def put(self, evt):
        self.queue.put_nowait(evt)

    def register(self, typ, cbs):
        setattr(self.cbs, typ, cbs)

    def start(self):
        launch(self.loop)

    def stop(self):
        self.stopped.set()


class Client(Handler):

    def __init__(self):
        Handler.__init__(self)
        self.register("command", command)

    def announce(self, txt):
        self.raw(txt)

    def say(self, channel, txt):
        self.raw(txt)

    def show(self, evt):
        for txt in evt.result:
            self.say(evt.channel, txt)

    def raw(self, txt):
        pass


"utility"


def cmnd(txt, out):
    clt = Client()
    clt.raw = out
    evn = Message()
    evn.orig = object.__repr__(clt)
    evn.txt = txt
    command(evn)
    evn.wait()
    return evn


def command(evt):
    parse_cmd(evt)
    func = getattr(Command.cmds, evt.cmd, None)
    if func:
        try:
            func(evt)
            evt.show()
        except Exception as exc:
            Error.add(exc)
    evt.ready()


def forever():
    while 1:
        try:
            time.sleep(1.0)
        except (KeyboardInterrupt, EOFError):
            _thread.interrupt_main()


def laps(seconds, short=True):
    txt = ""
    nsec = float(seconds)
    if nsec < 1:
        return f"{nsec:.2f}s"
    yea = 365*24*60*60
    week = 7*24*60*60
    nday = 24*60*60
    hour = 60*60
    minute = 60
    yeas = int(nsec/yea)
    nsec -= yeas*yea
    weeks = int(nsec/week)
    nsec -= weeks*week
    nrdays = int(nsec/nday)
    nsec -= nrdays*nday
    hours = int(nsec/hour)
    nsec -= hours*hour
    minutes = int(nsec/minute)
    nsec -= int(minute*minutes)
    sec = int(nsec)
    if yeas:
        txt += f"{yeas}y"
    if weeks:
        nrdays += weeks * 7
    if nrdays:
        txt += f"{nrdays}d"
    if short and txt:
        return txt.strip()
    if hours:
        txt += f"{hours}h"
    if minutes:
        txt += f"{minutes}m"
    if sec:
        txt += f"{sec}s"
    txt = txt.strip()
    return txt


def parse_cmd(obj, txt=None):
    args = []
    obj.args    = obj.args or []
    obj.cmd     = obj.cmd or ""
    obj.gets    = obj.gets or Default()
    obj.hasmods = obj.hasmod or False
    obj.index   = None
    obj.mod     = obj.mod or ""
    obj.opts    = obj.opts or ""
    obj.result  = obj.reult or []
    obj.sets    = obj.sets or Default()
    obj.txt     = txt or obj.txt or ""
    obj.otxt    = obj.txt
    _nr = -1
    for spli in obj.otxt.split():
        if spli.startswith("-"):
            try:
                obj.index = int(spli[1:])
            except ValueError:
                obj.opts += spli[1:]
            continue
        if "==" in spli:
            key, value = spli.split("==", maxsplit=1)
            if key in obj.gets:
                val = getattr(obj.gets, key)
                value = val + "," + value
            setattr(obj.gets, key, value)
            continue
        if "=" in spli:
            key, value = spli.split("=", maxsplit=1)
            if key == "mod":
                obj.hasmods = True
                if obj.mod:
                    obj.mod += f",{value}"
                else:
                    obj.mod = value
                continue
            setattr(obj.sets, key, value)
            continue
        _nr += 1
        if _nr == 0:
            obj.cmd = spli
            continue
        args.append(spli)
    if args:
        obj.args = args
        obj.txt  = obj.cmd or ""
        obj.rest = " ".join(obj.args)
        obj.txt  = obj.cmd + " " + obj.rest
    else:
        obj.txt = obj.cmd or ""



def scan(pkg, modstr, initer=False, disable="", wait=True):
    mds = []
    for modname in spl(modstr):
        if modname in spl(disable):
            continue
        module = getattr(pkg, modname, None)
        if not module:
            continue
        for _key, cmd in inspect.getmembers(module, inspect.isfunction):
            if 'event' in cmd.__code__.co_varnames:
                Command.add(cmd)
        for _key, clz in inspect.getmembers(module, inspect.isclass):
            if not issubclass(clz, Object):
                continue
            Persist.add(clz)
        if initer and "init" in dir(module):
            module._thr = launch(module.init, name=f"init {modname}")
            mds.append(module)
    if wait and initer:
        for mod in mds:
            mod._thr.join()
    return mds
