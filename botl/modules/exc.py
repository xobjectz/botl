# This file is placed in the Public Domain.
#
#


"excute"


from ..client  import command, parse_cmd
from ..command import Command
from ..job     import Job
from ..runtime import broker, pool


def exc(event):
    job = Job()
    parse_cmd(job, event.rest)
    bot = broker.get(event.orig)
    pool.put(command, bot, job)


Command.add(exc)