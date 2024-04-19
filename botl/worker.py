# This file is placed in the Public Domain.
#
#


"worker"


from .thread import Thread



class Worker(Thread):

    def __init__(self, thrname, *args, daemon=True, **kwargs):
        super().__init__(None, self.run, thrname, (), {}, daemon=daemon)
        self._result   = None
        self.name      = thrname
        self.queue     = queue.Queue()
        self.starttime = time.time()

    def put(self, func, *args, **kwargs):
        self.queue.put_nowait(func, *args, **kwargs)

    def run(self):
        "run this thread's payload."
        while not self.stopped:
            func, args = self.queue.get()
            try:
                self._result = func(*args)
            except Exception as ex:
                later(ex)
                if args and "Event" in str(type(args[0])):
                    args[0].ready()


def create():
    "launch a thread."
    worker = Worker()
    worker.start()
    return worker
