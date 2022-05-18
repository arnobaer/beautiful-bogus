from ..emulator import Emulator

__all__ = ["Marzhauser_Tango"]


class Marzhauser_Tango(Emulator):

    version = "3.61"

    version_string = "TANGO-EMULATOR, Version 1.00, Mar 11 2022, 13:51:01"

    tango_serial_number = "123456789"

    def __init__(self):
        super().__init__()

        self.add_route(r"^version$", lambda: type(self).version)
        self.add_route(r"^nversion$", lambda: type(self).version)
        self.add_route(r"^identity$", lambda: "TANGO-EMULATOR 0 0 0 0")
        self.add_route(r"^tango$", lambda: [type(self).version_string, type(self).tango_serial_number])  # multi-line

        # System configuration

        self.add_route(r"^reset$", lambda: None)
        self.add_route(r"^save$", lambda: None)
        self.add_route(r"^restore$", lambda: None)
