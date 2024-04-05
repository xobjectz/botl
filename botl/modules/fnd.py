# This file is placed in the Public Domain.
#
# pylint: disable=C,R,W0105,W0611


"find"


from ..client  import Client
from ..object  import fmt
from ..persist import Persist, Workdir, find


def fnd(event):
    "find objects."
    Workdir.skel()
    if not event.rest:
        res = sorted([x.split('.')[-1].lower() for x in Workdir.types()])
        if res:
            event.reply(",".join(res))
        return
    otype = event.args[0]
    clz = Persist.long(otype)
    if "." not in clz:
        for fnm in Workdir.types():
            claz = fnm.split(".")[-1]
            if otype == claz.lower():
                clz = fnm
    nmr = 0
    for fnm, obj in find(clz, event.gets):
        event.reply(f"{nmr} {fmt(obj)}")
        nmr += 1
    if not nmr:
        event.reply("no result")


"register"


#Client.add(fnd)
