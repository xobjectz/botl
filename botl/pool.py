# This file is placed in the Public Domain.
#
#


"pool"


import multiprocessing as mp
import random


from .client  import command
from .errors  import debug
from .job     import Job
from .object  import Object, keys, values
from .worker  import Worker


rpr = object.__repr__


class Pool:

    workers = Object()

    @staticmethod
    def add(worker):
        setattr(Pool.workers, rpr(worker), worker)       

    @staticmethod
    def init():
        ctx = mp.get_context("spawn")
        nrs = ctx.cpu_count()
        debug(f"{nrs} cpu detected")
        for nr in range(nrs):
            worker = Worker()
            worker.start()
            Pool.add(worker)

    @staticmethod
    def put(func, *args, **kwargs):
        for worker in values(Pool.workers):
            if worker.queue.empty():
                debug(f"{worker} {func}")
                worker.put(func, *args, **kwargs)
                return
        prockey = random.choice(keys(Pool.workers))
        proc = Pool.workers[prockey]
        proc.put(func, *args, **kwargs)
