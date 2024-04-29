# This file is placed in the Public Domain.


"available modules"


import os


def mod(event):
    "show available modules."
    path = os.path.dirname(__file__)
    event.reply(",".join(sorted([x[:-3] for x in os.listdir(path) if not x.startswith("__")])))
