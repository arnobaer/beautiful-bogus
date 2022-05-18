import unittest

from . import BaseTestCase


class Keithley2470Test(BaseTestCase):

    MODEL = "Keithley_2470"

    def test_basic(self):
        self.assertEqual(self.dispatch("*IDN?"), "Keithley Inc., Model 2470, 12345678, v1.0 (Emulator)")

        self.assertEqual(self.dispatch(":SOUR:VOLT:LEV?"), "+0.000E+00")
        self.assertEqual(self.dispatch("SOUR:VOLT:LEV 42"), None)
        self.assertEqual(self.dispatch(":SOUR:VOLT?"), "+4.200E+01")
        self.assertEqual(self.dispatch("*RST"), None)
        self.assertEqual(self.dispatch("SOUR:VOLT?"), "+0.000E+00")
