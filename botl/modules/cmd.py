# This file is placed in the Public Domain.
#
#


"cmd"


from ..client import Client


def cmd(event):
    "list of commands."
    event.reply(",".join(sorted(list(Client.cmds))))


Client.add(cmd)
