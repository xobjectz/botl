# This file is placed in the Public Domain.
#
# pylint: disable=C0103,C0116,E0402,R0401


"modules"


from . import __dir__


def mod(event):
    event.reply(",".join(__dir__()))
