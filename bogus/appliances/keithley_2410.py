from ..emulator import Property, Emulator

__all__ = ["Keithley_2410"]


class Keithley_2410(Emulator):

    def __init__(self):
        super().__init__()

        self.source_voltage_level = Property(0, type=float, format='+.3E')
        self.source_current_level = Property(0, type=float, format='+.3E')

        self.add_route(r"^\*IDN\?$", lambda: "Keithley Inc., Model 2410, 12345678, v1.0 (Emulator)")

        self.add_route(r'^\*RST$', self.handle_reset)
        self.add_route(r'^\*CLS$', self.handle_clear)

        self.add_route(r'^:?SOUR:VOLT(?::LEV)?\?$', self.source_voltage_level)
        self.add_route(r'^:?SOUR:VOLT(?::LEV)?\s+(.+)$', self.source_voltage_level)

        self.add_route(r'^:?SOUR:CURR(?::LEV)?\?$', self.source_current_level)
        self.add_route(r'^:?SOUR:CURR(?::LEV)?\s+(.+)$', self.source_current_level)

    def handle_reset(self):
        self.source_voltage_level.reset()
        self.source_current_level.reset()

    def handle_clear(self):
        ...
