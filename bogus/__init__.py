import importlib

__version__ = "0.1.0"


def load(name: str) -> object:
    """Load emulator class by it's name.

    >>> from emu import load
    >>> e = load("keithley_2410")()
    >>> e.dispatch("*RST")
    """
    module = importlib.import_module(f"bogus.appliances.{name.lower()}")
    for key, value in module.__dict__.items():
        if key.lower() == name.lower():
            return value
    raise KeyError(name)
