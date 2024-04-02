# This file is placed in the Public Domain.
#
# pylint: disable=R0902,R0903


"default"


from .object import Object


class Default(Object):

    "Default"

    __slots__ = ("__default__",)

    def __init__(self):
        Object.__init__(self)
        self.__default__ = ""

    def __getattr__(self, key):
        return self.__dict__.get(key, self.__default__)


def __dir__():
    return (
        'Default',
    )


__all__ = __dir__()
