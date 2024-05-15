# This file is placed in the Public Domain.
#
#


"utilities"


import datetime


def hms():
    "return hour:minutes:seconds string."
    return now().split(".")[0]


def date():
    "return time with date."
    return str(datetime.datetime.now())


def now():
    "return string of the current time."
    return date().split()[-1]
