# This file is placed in the Public Domain.
#
# pylint: disable=C0301


"slogan"


TXT = """By law, with the use of poison, killing, torturing, castrating, destroying in whole or in part,
all elderly and all handicapped (Wzd), all criminals (Wfz) and all psychiatric patients (WvGGZ)
here in the Netherlands."""


def lne(event):
    "diplay first line of slogan."
    event.reply(TXT.split("\n", maxsplit=1)[0])


def slg(event):
    "slogan"
    event.reply(TXT)
