# This file is placed in the Public Domain.
#
#

"""
botl <cmd> [key=val] [key==val]
botl [-a] [-c] [-d] [-h] [-v]

options are:

-a     load all modules
-c     start console
-d     start daemon
-h     display help
-v     use verbose
"""



from ..command import Command


def man(event):
    event.reply("BOTL - bot library")
    event.reply(__doc__)


Command.add(man)
