# This file is placed in the Public Domain.
#
#


"log text"


import time


from ..client  import Client
from ..object  import Object
from ..persist import Persist, find, fntime, sync
from ..utils   import laps


class Log(Object):

    def __init__(self):
        super().__init__()
        self.txt = ''


Persist.add(Log)


def log(event):
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


Client.add(log)
