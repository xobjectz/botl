# This file is placed in the Public Domain.
#
# pylint: disable=C,R,W0105


"mailbox"


import mailbox
import os
import time


from ..client  import Client
from ..object  import Object, fmt, update
from ..persist import Persist, find, fntime, sync
from ..utils   import laps


MONTH = {
    'Jan': 1,
    'Feb': 2,
    'Mar': 3,
    'Apr': 4,
    'May': 5,
    'Jun': 6,
    'Jul': 7,
    'Aug': 8,
    'Sep': 9,
    'Oct': 10,
    'Nov': 11,
    'Dec': 12
}


class Email(Object):

    "Email"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.text = ""

    def __ok__(self):
        pass

    def __okok__(self):
        pass


def cor(event):
    "search correspondence."
    if not event.args:
        event.reply("cor <email>")
        return
    nrs = -1
    for _fn, email in find("email", {"From": event.args[0]}):
        nrs += 1
        txt = ""
        if len(event.args) > 1:
            txt = ",".join(event.args[1:])
        else:
            txt = "From,Subject"
        form = fmt(email, txt, plain=True)
        lapsed = laps(time.time() - fntime(email.__stp__))
        event.reply(f"{nrs} {form} {lapsed}")


def eml(event):
    "search email from recipient."
    if not event.args:
        event.reply("eml <searchtxtinemail>")
        return
    nrs = -1
    for fnm, obj in find("email"):
        if event.rest in obj.text:
            nrs += 1
            form = fmt(obj, "From,Subject")
            lapsed = laps(time.time() - fntime(fnm))
            event.reply(f"{nrs} {form} {lapsed}")


def mbx(event):
    "scan mailbox."
    if not event.args:
        return
    fnm = os.path.expanduser(event.args[0])
    event.reply(f"reading from {fnm}")
    nrs = 0
    if os.path.isdir(fnm):
        thing = mailbox.Maildir(fnm, create=False)
    elif os.path.isfile(fnm):
        thing = mailbox.mbox(fnm, create=False)
    else:
        return
    try:
        thing.lock()
    except FileNotFoundError:
        pass
    for mail in thing:
        email = Email()
        update(email, mail._headers) # pylint: disable=W0212
        email.text = ""
        for payload in mail.walk():
            if payload.get_content_type() == 'text/plain':
                email.text += payload.get_payload()
        email.text = email.text.replace("\\n", "\n")
        sync(eml)
        nrs += 1
    if nrs:
        event.reply(f"ok {nrs}")


"register"


Client.add(cor)
Client.add(eml)
Client.add(mbx)
Persist.add(Email)
