# This file is placed in the Public Domain.
#
# pylint: disable=C0116,W0105,E0402,E0611


"errors"


from objx import items
from botl import Broker, Error


def err(event):
    nmr = 0
    for bot in items(Broker):
        if 'state' in dir(bot):
            event.reply(str(bot.state))
            nmr += 1
    event.reply(f"status: {nmr} errors: {len(Error.errors)}")
    for exc in Error.errors:
        txt = Error.format(exc)
        for line in txt.split():
            event.reply(line)
