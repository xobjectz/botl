# This file is placed in the Public Domain.
#
# pylint: disable=C,R,W0212


"scanner"


import inspect


from objx import Object

from .command import Command
from .parsers import spl
from .storage import Storage
from .threads import launch


def __dir__():
    return (
        'scan',
    )


__all__ = __dir__()


def scan(pkg, modstr, initer=False, disable="", wait=True) -> []:
    mds = []
    for modname in spl(modstr):
        if modname in spl(disable):
            continue
        module = getattr(pkg, modname, None)
        if not module:
            continue
        for _key, cmd in inspect.getmembers(module, inspect.isfunction):
            if 'event' in cmd.__code__.co_varnames:
                Command.add(cmd)
        for _key, clz in inspect.getmembers(module, inspect.isclass):
            if not issubclass(clz, Object):
                continue
            Storage.add(clz)
        if initer and "init" in dir(module):
            module._thr = launch(module.init, name=f"init {modname}")
            mds.append(module)
    if wait and initer:
        for mod in mds:
            mod._thr.join()
    return mds
