# This file is placed in the Public Domain.
#
# pylint: disable=C,R,W0105,E0402


"working directory"


import os


from .object import Object, cdir


class Workdir(Object):

    "Workdir"

    wd = ""

    @staticmethod
    def skel():
        "create directory,"
        cdir(os.path.join(Workdir.wd, "store", ""))

    @staticmethod
    def store(pth=""):
        "return objects directory."
        return os.path.join(Workdir.wd, "store", pth)

    @staticmethod
    def strip(pth, nmr=3):
        "reduce to path with directory."
        return os.sep.join(pth.split(os.sep)[-nmr:])

    @staticmethod
    def types():
        "return types stored."
        return os.listdir(Workdir.store())


"interface"


def __dir__():
    return (
        'Workdir',
    )


__all__ = __dir__()
