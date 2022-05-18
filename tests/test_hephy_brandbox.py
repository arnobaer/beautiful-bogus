import unittest

from . import BaseTestCase


class HEPHYBrandBoxTest(BaseTestCase):

    MODEL = "HEPHY_BrandBox"

    def test_basic(self):
        self.assertEqual(self.dispatch("*IDN?"), "BrandBox, v2.0 (Emulator)")
        self.assertEqual(self.dispatch("*RST"), "OK")
        self.assertEqual(self.dispatch("*CLS"), "OK")
        self.assertEqual(self.dispatch("*STB?"), "0,0,0,0,0,0")
        self.assertEqual(self.dispatch("*STR?"), "0")
        self.assertEqual(self.dispatch("*OPC?"), "1")

    def test_debug(self):
        self.assertEqual(self.dispatch("DEBUG?"), "Err99")

    def test_channels(self):
        self.assertEqual(self.dispatch(":CLOS:STAT?"), "")
        self.assertEqual(self.dispatch(":OPEN:STAT?"), "A1,A2,B1,B2,C1,C2")
        self.assertEqual(self.dispatch(":CLOS C1,A1"), "OK")
        self.assertEqual(self.dispatch(":CLOS:STAT?"), "A1,C1")
        self.assertEqual(self.dispatch(":OPEN:STAT?"), "A2,B1,B2,C2")
        self.assertEqual(self.dispatch(":OPEN C1"), "OK")
        self.assertEqual(self.dispatch(":CLOS:STAT?"), "A1")
        self.assertEqual(self.dispatch(":OPEN:STAT?"), "A2,B1,B2,C1,C2")

        self.assertEqual(self.dispatch(":OPEN A1,A2,B1"), "OK")
        self.assertEqual(self.dispatch(":OPEN B2,C1,C2"), "OK")

        self.assertEqual(self.dispatch("GET:A ?"), "OFF,OFF")
        self.assertEqual(self.dispatch("GET:A1 ?"), "OFF")
        self.assertEqual(self.dispatch("GET:A2 ?"), "OFF")
        self.assertEqual(self.dispatch("GET:B ?"), "OFF,OFF")
        self.assertEqual(self.dispatch("GET:B1 ?"), "OFF")
        self.assertEqual(self.dispatch("GET:B2 ?"), "OFF")
        self.assertEqual(self.dispatch("GET:C ?"), "OFF,OFF")
        self.assertEqual(self.dispatch("GET:C1 ?"), "OFF")
        self.assertEqual(self.dispatch("GET:C2 ?"), "OFF")

        self.assertEqual(self.dispatch("SET:A2_ON"), "OK")
        self.assertEqual(self.dispatch("SET:B1_ON"), "OK")
        self.assertEqual(self.dispatch("SET:C_ON"), "OK")

        self.assertEqual(self.dispatch("GET:A ?"), "OFF,ON")
        self.assertEqual(self.dispatch("GET:A1 ?"), "OFF")
        self.assertEqual(self.dispatch("GET:A2 ?"), "ON")
        self.assertEqual(self.dispatch("GET:B ?"), "ON,OFF")
        self.assertEqual(self.dispatch("GET:B1 ?"), "ON")
        self.assertEqual(self.dispatch("GET:B2 ?"), "OFF")
        self.assertEqual(self.dispatch("GET:C ?"), "ON,ON")
        self.assertEqual(self.dispatch("GET:C1 ?"), "ON")
        self.assertEqual(self.dispatch("GET:C2 ?"), "ON")

        self.assertEqual(self.dispatch("SET:A_OFF"), "OK")
        self.assertEqual(self.dispatch("SET:B_OFF"), "OK")
        self.assertEqual(self.dispatch("SET:C1_OFF"), "OK")
        self.assertEqual(self.dispatch("SET:C2_OFF"), "OK")

        self.assertEqual(self.dispatch("GET:A ?"), "OFF,OFF")
        self.assertEqual(self.dispatch("GET:A1 ?"), "OFF")
        self.assertEqual(self.dispatch("GET:A2 ?"), "OFF")
        self.assertEqual(self.dispatch("GET:B ?"), "OFF,OFF")
        self.assertEqual(self.dispatch("GET:B1 ?"), "OFF")
        self.assertEqual(self.dispatch("GET:B2 ?"), "OFF")
        self.assertEqual(self.dispatch("GET:C ?"), "OFF,OFF")
        self.assertEqual(self.dispatch("GET:C1 ?"), "OFF")
        self.assertEqual(self.dispatch("GET:C2 ?"), "OFF")

        self.assertEqual(self.dispatch(":CLOS:STAT?"), "")
        self.assertEqual(self.dispatch("*STB?"), "0,0,0,0,0,0")

    def test_mod(self):
        self.assertEqual(self.dispatch("GET:MOD ?"), "N/A")
        self.assertEqual(self.dispatch("SET:MOD IV"), "OK")
        self.assertEqual(self.dispatch("GET:MOD ?"), "IV")
        self.assertEqual(self.dispatch("SET:MOD CV"), "OK")
        self.assertEqual(self.dispatch("GET:MOD ?"), "CV")
        self.assertEqual(self.dispatch("SET:MOD CC"), "Err99")
        self.assertEqual(self.dispatch("GET:MOD ?"), "CV")

    def test_test_state(self):
        self.assertEqual(self.dispatch("GET:TST ?"), "OFF")
        self.assertEqual(self.dispatch("SET:TST ON"), "OK")
        self.assertEqual(self.dispatch("GET:TST ?"), "ON")
        self.assertEqual(self.dispatch("SET:TST OFF"), "OK")
        self.assertEqual(self.dispatch("GET:TST ?"), "OFF")
