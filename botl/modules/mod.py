# This file is placed in the Public Domain.
#
# pylint: disable=C,R


"available modules"


from ..client import Client


from . import __dir__


def mod(event):
    "list modules."
    event.reply(",".join(sorted(__dir__())))


Client.add(mod)
