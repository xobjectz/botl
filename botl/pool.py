# This file is placed in the Public Domain.
#
#


"pool"


import multiprocessing as mp
import random


from .errors import debug
from .job    import Job
from .object import Object, values
from .worker import Worker


rpr = object.__repr__


class Pool:

    procs = Object()

    @staticmethod
    def add(proc):
        debug(f"adding proces {len(Pool.procs)+1}") 
        setattr(Pool.procs, rpr(proc), proc)       

    @staticmethod
    def init():
        ctx = mp.get_context("spawn")
        print(dir(ctx))
        nrs = ctx.cpu_count()
        debug(f"{nrs} cpu detected")
        for nr in range(nrs):
            worker = Worker()
            process = ctx.Process(target=Worker.run)
            Pool.add(process)
            process.start()

    @staticmethod
    def put(func, *args, **kwargs):
        for proc in values(Pool.procs):
            if proc.queue.empty:
                proc.put(func, *args, **kwargs)
                return
        proc = random.choose(values(procs))
        proc.put(func, *args, **kwargs)
