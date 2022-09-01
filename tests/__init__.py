import pytest

from bogus import load

__all__ = ["TestModel"]


class TestModel:

    MODEL = None

    @pytest.fixture()
    def e(self):
        yield load(type(self).MODEL)()
