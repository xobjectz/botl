# This file is placed in the Public Domain.
#
#


"process"


from ..runtime import pool


def prc(event):
    for proc in pool.procs:
        event.reply(f"{proc}")
