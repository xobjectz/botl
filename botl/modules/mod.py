# This file is placed in the Public Domain.
#
# pylint: disable=C,R,W0105


"available modules"


from ..client import Client


from . import __dir__


def mod(event):
    "list modules."
    event.reply(",".join(sorted(__dir__())))


"register"


Client.add(mod)
