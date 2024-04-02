# This file is placed in the Public Domain.
#
#


"available modules"


from ..client import Client


from . import __dir__


def mod(event):
    event.reply(",".join(sorted(__dir__())))


Client.add(mod)
