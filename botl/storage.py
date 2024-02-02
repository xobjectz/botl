# This file is placed in the Public Domain.
#
# pylint: disable=C,R,W0105,E0402


"database"


import datetime
import pathlib
import os
import time
import _thread


from objx import Object, dump, fqn, load, items, update


from .handler import Default
from .parsers import spl


def __dir__():
    return (
        'Storage',
        'cdir',
        'fetch',
        'find',
        'fntime',
        'ident',
        'last',
        'read',
        'search',
        'sync',
        'write'
    )


__all__ = __dir__()


lock = _thread.allocate_lock()


def cdir(pth) -> None:
    if os.path.exists(pth):
        return
    pth = pathlib.Path(pth)
    os.makedirs(pth, exist_ok=True)


class Storage(Object):

    classes = {}
    wd = ""

    @staticmethod
    def add(clz):
        if not clz:
            return
        name = str(clz).split()[1][1:-2]
        Storage.classes[name] = clz

    @staticmethod
    def fns(mtc=""):
        dname = ''
        pth = Storage.store(mtc)
        for rootdir, dirs, _files in os.walk(pth, topdown=False):
            if dirs:
                for dname in sorted(dirs):
                    if dname.count('-') == 2:
                        ddd = os.path.join(rootdir, dname)
                        fls = sorted(os.listdir(ddd))
                        for fll in fls:
                            yield strip(os.path.join(ddd, fll))

    @staticmethod
    def long(name):
        split = name.split(".")[-1].lower()
        res = name
        for named in Storage.classes:
            if split in named.split(".")[-1].lower():
                res = named
                break
        if "." not in res:
            for fnm in Storage.types():
                claz = fnm.split(".")[-1]
                if fnm == claz.lower():
                    res = fnm
        return res

    @staticmethod
    def skel():
        cdir(os.path.join(Storage.wd, "store", ""))

    @staticmethod
    def store(pth=""):
        return os.path.join(Storage.wd, "store", pth)

    @staticmethod
    def types():
        return os.listdir(Storage.store())


def find(mtc, selector=None, index=None, deleted=False):
    clz = Storage.long(mtc)
    nr = -1
    for fnm in sorted(Storage.fns(clz), key=fntime):
        obj = Default()
        fetch(obj, fnm)
        if not deleted and '__deleted__' in obj:
            continue
        if selector and not search(obj, selector):
            continue
        nr += 1
        if index is not None and nr != int(index):
            continue
        yield (fnm, obj)


def fntime(daystr):
    daystr = daystr.replace('_', ':')
    datestr = ' '.join(daystr.split(os.sep)[-2:])
    if '.' in datestr:
        datestr, rest = datestr.rsplit('.', 1)
    else:
        rest = ''
    timed = time.mktime(time.strptime(datestr, '%Y-%m-%d %H:%M:%S'))
    if rest:
        timed += float('.' + rest)
    return timed


def strip(pth, nmr=3):
    return os.sep.join(pth.split(os.sep)[-nmr:])


def ident(obj):
    return os.path.join(
                        fqn(obj),
                        os.path.join(*str(datetime.datetime.now()).split())
                       )

def fetch(obj, pth):
    pth2 = Storage.store(pth)
    read(obj, pth2)
    return strip(pth)


def last(obj, selector=None):
    if selector is None:
        selector = {}
    result = sorted(
                    find(fqn(obj), selector),
                    key=lambda x: fntime(x[0])
                   )
    if result:
        inp = result[-1]
        update(obj, inp[-1])
        return inp[0]


def read(obj, pth):
    with lock:
        with open(pth, 'r', encoding='utf-8') as ofile:
            update(obj, load(ofile))


def search(obj, selector):
    res = False
    if not selector:
        return True
    for key, value in items(selector):
        if key not in obj:
            res = False
            break
        for vval in spl(str(value)):
            val = getattr(obj, key, None)
            if str(vval).lower() in str(val).lower():
                res = True
            else:
                res = False
                break
    return res


def sync(obj, pth=None):
    if pth is None:
        pth = ident(obj)
    pth2 = Storage.store(pth)
    write(obj, pth2)
    return pth


def write(obj, pth):
    with lock:
        cdir(os.path.dirname(pth))
        with open(pth, 'w', encoding='utf-8') as ofile:
            dump(obj, ofile, indent=4)
