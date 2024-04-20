# This file is placed in the Public Domain.
#
#


"worker"


import multiprocessing as mp


import queue
import threading
import _thread


from .errors import later


class Worker(mp.Process):

    queue = queue.Queue()

    @staticmethod
    def put(func, *args, **kwargs):
        "put job on queue."
        Worker.queue.put_nowait((func, args))

    @staticmethod
    def run():
        "run mainloop."
        while 1:
            try:
                func, args = Worker.queue.get()
            except KeyboardInterrupt:
                return
            try:
                func(*args)
            except Exception as ex:
                later(ex)
                if args:
                    try:
                        args[0].ready()
                    except AttributeError:
                        pass
