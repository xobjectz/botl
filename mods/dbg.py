# This file is in the Public Domain.
#
#

from botl.objects import fmt


def dbg(event):
    raise Exception(fmt(event))
