# This file is placed in the Public Domain.
#
# pylint: disable=C,R,W0105


"job"


from .default import Default


class Job(Default):

    "Job"

    def __init__(self):
        Default.__init__(self)
        self.result  = []

    def reply(self, txt):
        "add text to the result"
        self.result.append(txt)
