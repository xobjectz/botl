# This file is placed in the Public Domain.
#
#


"pool"


from .objects import Object
from .thread  import create


def rpr = object.__repr__


class ThreadBroker:


    threads = Object()

    @staticmethod
    def add(obj):
        "add an object to the broker."
        setattr(ThreadBroker.threads, rpr(obj), obj)

    @staticmethod
    def first():
        "return first object."
        for key in keys(self.objs):
            return getattr(ThreadBroker.threads, key)

    @staticmethod
    def init(nr=6):
        for _nr in range(nr):
            ThreadBroker.add(create())

    @staticmethod
    def get(orig):
        "return object by origin (repr)"
        return getattr(ThreadBroker.threads, orig, None)

    @staticmethod
    def put(evt):
         for thr in Threadpool.threads:
             if not thr.busy:
                 thr.put(evt)
                 break

    @staticmethod
    def remove(obj):
        "remove object from broker"
        delattr(ThreadBroker.threads, rpr(obj))
