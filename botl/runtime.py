# This file is placed in the Public Domain.


"runtime"


import os
import time


from .broker    import Broker
from .client    import spl
from .errors    import later
from .command   import scan as scancmd
from .whitelist import scan as scancls


broker = Broker()
dte    = time.ctime(time.time()).replace("  ", " ")
path   = os.path.join(os.path.dirname(__file__), "modules")
mods   = ",".join(sorted([x[:-3] for x in os.listdir(path) if not x.startswith("__")]))


def init(pkg, modstr, disable=""):
    "start modules"
    mds = []
    for modname in spl(modstr):
        if doskip(modname, disable):
            continue
        mod = getattr(pkg, modname, None)
        if not mod:
            continue
        if "init" in dir(mod):
            try:
                mod.init()
                mds.append(mod)
            except Exception as ex: # pylint: disable=W0718
                later(ex)
    return mds


def scan(pkg, modstr, disable=""):
    "scan modules for commands and classes"
    mds = []
    for modname in spl(modstr):
        if doskip(modname, disable):
            continue
        module = getattr(pkg, modname, None)
        if not module:
            continue
        scancmd(module)
        scancls(module)
    return mds


def doskip(name, skipp):
    "check for skipping"
    for skp in spl(skipp):
        if skp in name:
            return True
    return False



def __dir__():
    return (
        'broker',
        'dte',
        'init',
        'scan'
    )
