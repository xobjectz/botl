# This file is placed in the Public Domain.
#
#


"worker"


import multiprocessing as mp


import queue
import threading
import _thread


from .errors import later


class Worker:

    queue = mp.Queue()

    @staticmethod
    def put(func, *args, **kwargs):
        "put job on queue."
        Worker.queue.put_nowait(func, *args, **kwargs)

    @staticmethod
    def run():
        "run mainloop."
        while 1:
            try:
                func, args = Worker.queue.get()
                self._result = func(*args)
            except KeyboardInterrupt:
                return
            except Exception as ex:
                later(ex)
                if args:
                    try:
                        args[0].ready()
                    except AttributeError:
                        pass
