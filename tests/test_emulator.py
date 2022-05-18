import unittest

from bogus.emulator import Property, Route, Emulator


class EmulatorTest(unittest.TestCase):

    def test_basic(self):
        e = Emulator()

        def reset():
            e.voltage.reset()

        e.voltage = Property(0, type=float, format="+.3E")
        e.add_route(r"^\*RST$", reset)
        e.add_route(r"^VOLT\?$", e.voltage)
        e.add_route(r"^VOLT\s(.+)$", e.voltage)

        self.assertEqual(e.dispatch("VOLT?"), "+0.000E+00")
        self.assertEqual(e.dispatch("VOLT 42"), None)
        self.assertEqual(e.dispatch("VOLT?"), "+4.200E+01")
        self.assertEqual(e.dispatch("*RST"), None)
        self.assertEqual(e.dispatch("VOLT?"), "+0.000E+00")
