# This file is placed in the Public Domain.
#
# pylint: disable=C,R,W0105,W0611


"debug"


from ..client import Client


class MyBug(Exception):

    "MyBug"


def dbg(event):
    "raise exception"
    raise MyBug("yo!")


"register"


#Client.add(dbg)
