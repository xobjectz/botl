# This file is placed in the Public Domain.
#
# pylint: disable=C,R


"debug"


from ..client import Client


class MyBug(Exception):

    "MyBug"


def dbg(event):
    "raise exception"
    raise MyBug("yo!")


Client.add(dbg)
