# This file is placed in the Public Domain.
#
# pylint: disable=C,R,W0105


"event"


import threading


from .default import Default


class Event(Default):

    "Event"

    def __init__(self):
        Default.__init__(self)
        self._ready  = threading.Event()
        self.done    = False
        self.orig    = None
        self.result  = []
        self.thr    = None
        self.txt     = ""
        self.type    = "event"

    def ready(self):
        "event is ready."
        self._ready.set()

    def reply(self, txt):
        "add text to the result"
        self.result.append(txt)

    def wait(self, sec=None):
        "wait for event to be ready."
        if self.thr:
            self.thr.join()
        self._ready.wait(sec)
        return self.result


"interface"


def __dir__():
    return (
        'Event',
    )


__all__ = __dir__()
