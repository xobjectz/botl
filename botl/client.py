# This file is placed in the Public Domain.
#
# pylint: disable=W0718


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
        func = getattr(Client.cmds, evt.cmd, None)
        if func:
            try:
                func(evt)
            except BaseException as exc:
                Errors.add(exc)
        self.show(evt)
        evt.ready()

    def raw(self, txt):
        "raw output."

    def say(self, channel, txt):
        "say text in a channel."
        if channel:
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


def __dir__():
    return (
        'Client',
        'cmnd'
    )


__all__ = __dir__()
