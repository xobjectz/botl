# This file is placed in the Public Domain.
#
# pylint: disable=C,R,W0718


"enable/disable"


from botl.excepts import Error
from botl.scanner import scan


import zbot


def __dir__():
    return (
       'dis',
       'ena'
    )


def dis(event):
    if not event.args:
        mods = ",".join(dir(zbot))
        event.reply(f"disable {mods}")
        return
    what = event.args[0]
    mod = getattr(zbot, what, None)
    if mod:
        func = getattr(mod, "shutdown", None)
        if func:
            try:
                func()
            except Exception as ex:
                Error.add(ex)


def ena(event):
    if not event.args:
        mods = ",".join(dir(zbot))
        event.reply(f"enable {mods}")
        return
    what = event.args[0]
    try:
        init = event.args[1]
    except IndexError:
        init = False
    scan(zbot, what, init)
