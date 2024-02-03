# This file is placed in the Public Domain.
#
# pylint: disable=C0116,E0402,E0401,W0105


"commands"


from botl import Command


def cmd(event):
    event.reply(",".join(sorted(Command.cmds)))
