# This file is placed in the Public Domain.
#
# pylint: disable=C,R,W0401,W0622,W0614,E0402,E0603


"""objects library


OBX provides an obx namespace that allows for easy json save//load
to/from disk of objects. It provides an "clean namespace" Object class
that only has dunder methods, so the namespace is not cluttered with
method names. This makes storing and reading to/from json possible.

    >>> from obx import Object, dumps, loads
    >>> o = Object()
    >>> o.a = "b"
    >>> txt = dumps(o)
    >>> loads(txt)
    {"a": "b"}

OBX is Public Domain."""


from .default import *
from .locates import *
from .objects import *
from .persist import *
from .workdir import *


def __dir__():
    return (
        'Default',
        'Object',
        'Workdir',
        'construct',
        'dump',
        'dumps',
        'edit',
        'fetch',
        'find',
        'fmt',
        'fntime',
        'fqn',
        'ident',
        'items',
        'keys',
        'last',
        'load',
        'loads',
        'read',
        'search',
        'spl',
        'sync',
        'update',
        'values',
        'write'
     )


__all__ = __dir__()
