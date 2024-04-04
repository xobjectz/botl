# This file is placed in the Public Domain.
#
# pylint: disable=C,R,W0105,W0718


"client"


from .broker  import Broker
from .errors  import Errors
from .event   import Event
from .handler import Handler
from .object  import Object
from .parser  import parse_cmd


class Client(Handler):

    "Client"

    cmds = Object()

    def __init__(self):
        Handler.__init__(self)
        self.register("command", self.command)
        Broker.add(self)

    @staticmethod
    def add(func):
        "add command to client."
        setattr(Client.cmds, func.__name__, func)

    def announce(self, txt):
        "announce text."
        self.raw(txt)

    def command(self, evt):
        "check for and run a command."
        parse_cmd(evt)
        func = getattr(self.cmds, evt.cmd, None)
        if func:
            try:
                func(evt)
                self.show(evt)
            except Exception as ex:
                Errors.add(ex)
        evt.ready()

    def raw(self, txt):
        "raw output."

    def say(self, _channel, txt):
        "say text in a channel."
        self.raw(txt)

    def show(self, evt):
        "show results into a channel."
        for txt in evt.result:
            self.say(evt.channel, txt)


def cmnd(txt, out):
    "do a command using the provided output function."
    clt = Client()
    clt.raw = out
    evn = Event()
    evn.orig = object.__repr__(clt)
    evn.txt = txt
    clt.command(evn)
    evn.wait()
    return evn


"interface"


def __dir__():
    return (
        'Client',
        'cmnd'
    )


__all__ = __dir__()
