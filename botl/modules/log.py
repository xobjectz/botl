# This file is placed in the Public Domain.
#
# pylint: disable=C,R,W0105


"log text"


import time


from ..client  import Client
from ..object  import Object
from ..persist import Persist, find, fntime, sync
from ..utils   import laps


class Log(Object):

    "Log"

    def __init__(self):
        Object.__init__()
        self.txt = ''

    def __yo__(self):
        pass

    def __yoyo__(self):
        pass


def log(event):
    "log text."
    if not event.rest:
        nmr = 0
        for fnm, obj in find('log'):
            lap = laps(time.time() - fntime(fnm))
            event.reply(f'{nmr} {obj.txt} {lap}')
            nmr += 1
        if not nmr:
            event.reply('no log')
        return
    obj = Log()
    obj.txt = event.rest
    sync(obj)
    event.reply('ok')


"register"

Client.add(log)
Persist.add(Log)
