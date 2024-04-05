# This file is placed in the Public Domain.
#
# pylint: disable=C,R,W0105


"todo list"


import time


from dataclasses import dataclass


from ..client  import Client
from ..object  import Object
from ..persist import Persist, fntime, find, sync
from ..utils   import laps


class NoDate(Exception):

    "NoDate"


@dataclass
class Todo(Object):

    "Todo"

    txt: str = ''


def dne(event):
    "mark todo as done."
    if not event.args:
        event.reply("dne <txt>")
        return
    selector = {'txt': event.args[0]}
    nmr = 0
    for fnm, obj in find('todo', selector):
        nmr += 1
        obj.__deleted__ = True
        sync(obj, fnm)
        event.reply('ok')
        break
    if not nmr:
        event.reply("nothing todo")


def tdo(event):
    "add a todo."
    if not event.rest:
        nmr = 0
        for fnm, obj in find('todo'):
            lap = laps(time.time()-fntime(fnm))
            event.reply(f'{nmr} {obj.txt} {lap}')
            nmr += 1
        if not nmr:
            event.reply("no todo")
        return
    obj = Todo()
    obj.txt = event.rest
    sync(obj)
    event.reply('ok')


"register"


Client.add(dne)
Client.add(tdo)
Persist.add(Todo)
