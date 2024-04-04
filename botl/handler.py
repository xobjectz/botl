# This file is placed in the Public Domain.
#
#


"handler"


import queue
import threading
import _thread


from .errors  import Errors
from .object  import Object
from .thread  import launch


class Handler:

    "Handler"

    def __init__(self):
        self.cbs = Object()
        self.queue    = queue.Queue()
        self.stopped  = threading.Event()
        self.threaded = True

    def callback(self, evt):
        "call callback based on event type."
        func = getattr(self.cbs, evt.type, None)
        if func:
            func(evt)

    def loop(self):
        "proces events until interrupted."
        while not self.stopped.is_set():
            try:
                evt = self.poll()
                self.callback(evt)
            except Exception as ex: # pylint: disable=W0718
                Errors.add(ex)
                evt.ready()
            except (KeyboardInterrupt, EOFError):
                _thread.interrupt_main()

    def poll(self):
        "function to return event."
        return self.queue.get()

    def put(self, evt):
        "put event into the queue."
        self.queue.put_nowait(evt)

    def register(self, typ, cbs):
        "register callback for a type."
        setattr(self.cbs, typ, cbs)

    def start(self):
        "start the event loop."
        launch(self.loop)

    def stop(self):
        "stop the event loop."
        self.stopped.set()


def __dir__():
    return (
        'Handler',
    )


__all__ = __dir__()
