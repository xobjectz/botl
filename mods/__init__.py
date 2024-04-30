# This file is placed in the Public Domain.
#
# pylint: disable=C,R
# ruff: noqa: F401


"modules"


import importlib
import os
import sys


SKIP = [
    "run"
]


modules = []


def __dir__():
    return sorted(modules)


def debug(txt):
    print(txt)


def getmain(name):
    mod = sys.modules.get("__main__")
    return getattr(mod, name, None)


def import_pkg(dname, pname=""):
    for pth in os.listdir(dname):
        if pth.startswith("__"):
            continue
        if not pth.endswith(".py"):
            continue
        nam = pth[:-3]
        if nam in SKIP:
            continue
        if pname:
            name = f"{pname}.{nam}"
        importlib.import_module(name)
        modules.append(nam)


import_pkg(os.path.dirname(__file__), "mods")
