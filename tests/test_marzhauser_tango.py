import unittest

from . import BaseTestCase


class MarzhauserTangoTest(BaseTestCase):

    MODEL = "Marzhauser_Tango"

    def test_basic(self):
        self.assertEqual(self.dispatch("version"), "3.61")
        self.assertEqual(self.dispatch("nversion"), "3.61")
        self.assertEqual(self.dispatch("identity"), "TANGO-EMULATOR 0 0 0 0")
        self.assertEqual(self.dispatch("tango"), ["TANGO-EMULATOR, Version 1.00, Mar 11 2022, 13:51:01", "123456789"])

    def test_system(self):
        self.assertEqual(self.dispatch("reset"), None)
        self.assertEqual(self.dispatch("save"), None)
        self.assertEqual(self.dispatch("restore"), None)
