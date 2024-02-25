# This file is placed in the Public Domain.
#
# pylint: disable=C,R


"runtime"


import getpass
import os
import sys


from objx.default import Default
from objx.excepts import Error
from objx.workdir import Workdir


from botl.clients import cmnd 
from botl.scanner import scan


from .utility import daemon, forever, privileges


Cfg         = Default()
Cfg.mod     = "cmd,irc,rss"
Cfg.name    = __file__.split(os.sep)[-2]
Cfg.wd      = os.path.expanduser(f"~/.{Cfg.name}")
Cfg.pidfile = os.path.join(Cfg.wd, f"{Cfg.name}.pid")
Cfg.user    = getpass.getuser()
Workdir.wd  = Cfg.wd


from . import modules


def cli():
    Cfg.mod = ",".join(modules.__dir__())
    scan(modules, Cfg.mod)
    cmnd(" ".join(sys.argv[1:]), print)
    Error.show()

def main():
    daemon(Cfg.pidfile)
    privileges(Cfg.user)
    scan(modules, Cfg.mod, True)
    forever()
