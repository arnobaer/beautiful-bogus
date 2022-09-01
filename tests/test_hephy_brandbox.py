from . import TestModel


class TestHEPHYBrandBox(TestModel):

    MODEL = "HEPHY_BrandBox"

    def test_basic(self, e):
        assert e.dispatch("*IDN?") == "BrandBox, v2.0 (Emulator)"
        assert e.dispatch("*RST") == "OK"
        assert e.dispatch("*CLS") == "OK"
        assert e.dispatch("*STB?") == "0,0,0,0,0,0"
        assert e.dispatch("*STR?") == "0"
        assert e.dispatch("*OPC?") == "1"

    def test_debug(self, e):
        assert e.dispatch("DEBUG?") == "Err99"

    def test_channels(self, e):
        assert e.dispatch(":CLOS:STAT?") == ""
        assert e.dispatch(":OPEN:STAT?") == "A1,A2,B1,B2,C1,C2"
        assert e.dispatch(":CLOS C1,A1") == "OK"
        assert e.dispatch(":CLOS:STAT?") == "A1,C1"
        assert e.dispatch(":OPEN:STAT?") == "A2,B1,B2,C2"
        assert e.dispatch(":OPEN C1") == "OK"
        assert e.dispatch(":CLOS:STAT?") == "A1"
        assert e.dispatch(":OPEN:STAT?") == "A2,B1,B2,C1,C2"

        assert e.dispatch(":OPEN A1,A2,B1") == "OK"
        assert e.dispatch(":OPEN B2,C1,C2") == "OK"

        assert e.dispatch("GET:A ?") == "OFF,OFF"
        assert e.dispatch("GET:A1 ?") == "OFF"
        assert e.dispatch("GET:A2 ?") == "OFF"
        assert e.dispatch("GET:B ?") == "OFF,OFF"
        assert e.dispatch("GET:B1 ?") == "OFF"
        assert e.dispatch("GET:B2 ?") == "OFF"
        assert e.dispatch("GET:C ?") == "OFF,OFF"
        assert e.dispatch("GET:C1 ?") == "OFF"
        assert e.dispatch("GET:C2 ?") == "OFF"

        assert e.dispatch("SET:A2_ON") == "OK"
        assert e.dispatch("SET:B1_ON") == "OK"
        assert e.dispatch("SET:C_ON") == "OK"

        assert e.dispatch("GET:A ?") == "OFF,ON"
        assert e.dispatch("GET:A1 ?") == "OFF"
        assert e.dispatch("GET:A2 ?") == "ON"
        assert e.dispatch("GET:B ?") == "ON,OFF"
        assert e.dispatch("GET:B1 ?") == "ON"
        assert e.dispatch("GET:B2 ?") == "OFF"
        assert e.dispatch("GET:C ?") == "ON,ON"
        assert e.dispatch("GET:C1 ?") == "ON"
        assert e.dispatch("GET:C2 ?") == "ON"

        assert e.dispatch("SET:A_OFF") == "OK"
        assert e.dispatch("SET:B_OFF") == "OK"
        assert e.dispatch("SET:C1_OFF") == "OK"
        assert e.dispatch("SET:C2_OFF") == "OK"

        assert e.dispatch("GET:A ?") == "OFF,OFF"
        assert e.dispatch("GET:A1 ?") == "OFF"
        assert e.dispatch("GET:A2 ?") == "OFF"
        assert e.dispatch("GET:B ?") == "OFF,OFF"
        assert e.dispatch("GET:B1 ?") == "OFF"
        assert e.dispatch("GET:B2 ?") == "OFF"
        assert e.dispatch("GET:C ?") == "OFF,OFF"
        assert e.dispatch("GET:C1 ?") == "OFF"
        assert e.dispatch("GET:C2 ?") == "OFF"

        assert e.dispatch(":CLOS:STAT?") == ""
        assert e.dispatch("*STB?") == "0,0,0,0,0,0"

    def test_mod(self, e):
        assert e.dispatch("GET:MOD ?") == "N/A"
        assert e.dispatch("SET:MOD IV") == "OK"
        assert e.dispatch("GET:MOD ?") == "IV"
        assert e.dispatch("SET:MOD CV") == "OK"
        assert e.dispatch("GET:MOD ?") == "CV"
        assert e.dispatch("SET:MOD CC") == "Err99"
        assert e.dispatch("GET:MOD ?") == "CV"

    def test_test_state(self, e):
        assert e.dispatch("GET:TST ?") == "OFF"
        assert e.dispatch("SET:TST ON") == "OK"
        assert e.dispatch("GET:TST ?") == "ON"
        assert e.dispatch("SET:TST OFF") == "OK"
        assert e.dispatch("GET:TST ?") == "OFF"
