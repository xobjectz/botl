# This file is placed in the Public Domain.
#
# pylint: disable=C,R


"configuration"


import getpass
import os


from objx.default import Default
from objx.workdir import Workdir


Cfg         = Default()
Cfg.mod     = "cmd,irc,rss"
Cfg.name    = __file__.split(os.sep)[-2]
Cfg.wd      = os.path.expanduser(f"~/.{Cfg.name}")
Cfg.pidfile = os.path.join(Cfg.wd, f"{Cfg.name}.pid")
Cfg.user    = getpass.getuser()
Workdir.wd  = Cfg.wd
