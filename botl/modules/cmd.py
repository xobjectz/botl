# This file is placed in the Public Domain.
#
# pylint: disable=C,R,W0105
 

"cmd"


from ..client import Client


def cmd(event):
    "list of commands."
    event.reply(",".join(sorted(list(Client.cmds))))


"register"


Client.add(cmd)
