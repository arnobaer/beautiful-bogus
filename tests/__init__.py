import unittest

from bogus import load

__all__ = ["BaseTestCase"]


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        self.emulator = load(type(self).MODEL)()

    def dispatch(self, message):
        return self.emulator.dispatch(message)
