# This file is placed in the Public Domain.
#
# pylint: disable=C,R,W0718,W0611,E0402


"commands"


from objx import Object


from .parsers import parse_cmd
from .threads import launch


def __dir__():
    return (
        "Command",
    )


__all__ = __dir__()


class Command(Object):

    cmds = Object()

    @staticmethod
    def add(func):
        setattr(Command.cmds, func.__name__, func)

    @staticmethod
    def handle(evt):
        parse_cmd(evt)
        func = getattr(Command.cmds, evt.cmd, None)
        if func:
            func(evt)
            evt.show()
        evt.ready()
