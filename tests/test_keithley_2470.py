from . import TestModel


class TestKeithley2470(TestModel):

    MODEL = "Keithley_2470"

    def test_basic(self, e):
        assert e.dispatch("*IDN?") == "Keithley Inc., Model 2470, 12345678, v1.0 (Emulator)"

        assert e.dispatch(":SOUR:VOLT:LEV?") == "+0.000E+00"
        assert e.dispatch("SOUR:VOLT:LEV 42") is None
        assert e.dispatch(":SOUR:VOLT?") == "+4.200E+01"
        assert e.dispatch("*RST") is None
        assert e.dispatch("SOUR:VOLT?") == "+0.000E+00"
