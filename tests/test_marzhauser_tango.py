from . import TestModel


class TestMarzhauserTango(TestModel):

    MODEL = "Marzhauser_Tango"

    def test_basic(self, e):
        assert e.dispatch("version") == "3.61"
        assert e.dispatch("nversion") == "3.61"
        assert e.dispatch("identity") == "TANGO-EMULATOR 0 0 0 0"
        assert e.dispatch("tango") == ["TANGO-EMULATOR, Version 1.00, Mar 11 2022, 13:51:01", "123456789"]

    def test_system(self, e):
        assert e.dispatch("reset") is None
        assert e.dispatch("save") is None
        assert e.dispatch("restore") is None
