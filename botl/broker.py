# This file is placed in the Public Domain.
#
# pylint: disable=C,R,W0105


"broker"


from .object import Object, keys, values


rpr = object.__repr__


class Broker:

    "Broker"

    objs = Object()

    @staticmethod
    def add(obj):
        "add an object to the broker."
        setattr(Broker.objs, rpr(obj), obj)

    @staticmethod
    def all():
        "return all objects."
        return values(Broker.objs)

    @staticmethod
    def first():
        "return first object."
        for key in keys(Broker.objs):
            return getattr(Broker.objs, key)

    @staticmethod
    def get(orig):
        "return object by origin (repr)"
        return getattr(Broker.objs, orig, None)

    @staticmethod
    def remove(obj):
        "remove object from broker"
        delattr(Broker.objs, rpr(obj))


"interface"


def __dir__():
    return (
        'Broker',
    )


__all__ = __dir__()
