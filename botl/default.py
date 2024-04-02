# This file is placed in the Public Domain.
#
# pylint: disable=C,R,W0105,W0613,E0101


"default values"


import json


from .object import Object


class Default(Object):

    "Default"

    __slots__ = ("__default__",)

    def __init__(self):
        Object.__init__(self)
        self.__default__ = ""

    def __getattr__(self, key):
        return self.__dict__.get(key, self.__default__)


"interface"


def __dir__():
    return (
        'Default',
    )


__all__ = __dir__()
