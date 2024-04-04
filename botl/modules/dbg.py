# This file is placed in the Public Domain.
#
#


"debug"


from ..client import Client


class MyBug(Exception):

    "MyBug"


def dbg(event):
    "raise exception"
    raise MyBug("yo!")


#Client.add(dbg)
