# This file is placed in the Public Domain.
#
# pylint: disable=C,R,W0105


"status of bots"


from ..broker  import Broker
from ..client  import Client
from ..errors  import Errors


def err(event):
    "show errors."
    nmr = 0
    for bot in Broker.all():
        if 'state' in dir(bot):
            event.reply(str(bot.state))
            nmr += 1
    event.reply(f"status: {nmr} errors: {len(Errors.errors)}")
    for exc in Errors.errors:
        txt = Errors.format(exc)
        for line in txt.split():
            event.reply(line)


"register"


Client.add(err)
