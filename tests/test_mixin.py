# This file is placed in the Public Domain.
#
#
# pylint: disable=C,R,W1503


"mixin"


import unittest


from botl.object import Object


class Mix:
   a = "b"


class Mixin(Mix, Object):
    pass


class TestMixin(unittest.TestCase):

    def test_mixin(self):
        m = Mixin()
        self.assertTrue(type(m) == Mixin)
