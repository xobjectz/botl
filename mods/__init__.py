# This file is placed in the Public Domain.
#
# ruff: noqa: F401


"modules"


import importlib
import os


dirname = os.path.dirname(__file__)
pkgname = dirname.split(os.sep)[-1]
modules =  []


def __dir__():
    return modules

for path in os.listdir(dirname):
    if path.startswith("__"):
        continue
    if not path.endswith(".py"):
        continue
    name = path[:-3]
    mod = importlib.import_module(f"{pkgname}.{name}", pkgname)
    modules.append(name)
