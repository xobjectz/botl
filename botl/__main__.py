# This file is placed in the Public Domain.
#
# pylint: disable=C,R,W0105,W0212
# ruff: noqa: E402


"main"


import getpass
import os
import pwd
import sys
import termios
import time


from .client  import Client, cmnd
from .default import Default
from .errors  import Errors,debug
from .event   import Event
from .object  import cdir
from .parser  import parse_cmd
from .utils   import spl
from .workdir import Workdir


from . import modules

Cfg          = Default()
Cfg.mod      = "cmd,mod"
Cfg.name     = sys.argv[0].split(os.sep)[-2]
Cfg.dir      = os.path.expanduser(f"~/.{Cfg.name}")
Cfg.pidfile  = os.path.join(Cfg.wd, f"{Cfg.name}.pid")
Workdir.workdir = Cfg.dir


dte = time.ctime(time.time()).replace("  ", " ")
ext = os._exit 


class Console(Client):

    "Console"

    def announce(self, txt):
        "blind announce"

    def callback(self, evt):
        "run and wait for callback to finish."
        Client.callback(self, evt)
        evt.wait(5.0)

    def poll(self):
        "reconstruct event from input."
        evt = Event()
        evt.orig = object.__repr__(self)
        evt.txt = input("> ")
        evt.type = "command"
        return evt

    def say(self, _channel, txt):
        "say text in channel."
        txt = txt.encode('utf-8', 'replace').decode()
        print(txt)


def daemon(pidfile, verbose=False):
    "fork into the background."
    pid = os.fork()
    if pid != 0:
        ext(0)
    os.setsid()
    pid2 = os.fork()
    if pid2 != 0:
        ext(0)
    if not verbose:
        with open('/dev/null', 'r', encoding="utf-8") as sis:
            os.dup2(sis.fileno(), sys.stdin.fileno())
        with open('/dev/null', 'a+', encoding="utf-8") as sos:
            os.dup2(sos.fileno(), sys.stdout.fileno())
        with open('/dev/null', 'a+', encoding="utf-8") as ses:
            os.dup2(ses.fileno(), sys.stderr.fileno())
    os.umask(0)
    os.chdir("/")
    if os.path.exists(pidfile):
        os.unlink(pidfile)
    cdir(os.path.dirname(pidfile))
    with open(pidfile, "w", encoding="utf-8") as fds:
        fds.write(str(os.getpid()))


def init(pkg, modstr, disable=""):
    "start inits in modules."
    mds = []
    for modname in spl(modstr):
        if modname in spl(disable):
            continue
        module = getattr(pkg, modname, None)
        if not module:
            continue
        if "init" in dir(module):
            module.init()
            mds.append(module)
    return mds


def privileges(username):
    "lower privileges."
    pwnam = pwd.getpwnam(username)
    os.setgid(pwnam.pw_gid)
    os.setuid(pwnam.pw_uid)


def wrap(func):
    "restore terminal"
    old2 = None
    try:
        old2 = termios.tcgetattr(sys.stdin.fileno())
    except termios.error:
        pass
    try:
        func()
    except (KeyboardInterrupt, EOFError):
        print("")
    finally:
        if old2:
            termios.tcsetattr(sys.stdin.fileno(), termios.TCSADRAIN, old2)


"runtime"


def main():
    "main code"
    Workdir.skel()
    Errors.enable(print)
    parse_cmd(Cfg, " ".join(sys.argv[1:]))
    result = None
    if 'a' in Cfg.opts:
        Cfg.mod = "," + ",".join(modules.__dir__())
    if "v" in Cfg.opts:
        debug(f"{Cfg.name.upper()} {Cfg.opts.upper()} started {dte}")
    if "h" in Cfg.opts:
        print(__doc__)
        return result
    if "d" in Cfg.opts:
        Cfg.mod = ",".join(modules.__dir__())
        Cfg.user = getpass.getuser()
        daemon(Cfg.pidfile, "v" in Cfg.opts)
        privileges(Cfg.user)
        init(modules, Cfg.mod)
        while 1:
            time.sleep(1.0)
    elif "c" in Cfg.opts:
        init(modules, Cfg.mod)
        csl = Console()
        csl.start()
        while 1:
            time.sleep(1.0)
    elif Cfg.otxt:
        cmnd(Cfg.otxt, print)
    return result


def wrapped():
    "wrapped code"
    wrap(main)
    Errors.show()


if __name__ == "__main__":
    wrapped()
