from typing import Set

from ..emulator import Emulator

__all__ = ["HEPHY_BrandBox"]


def split_channels(channels: str) -> set:
    return {channel.strip() for channel in channels.split(',') if channel.strip()}


def join_channels(channels: set) -> str:
    return ','.join([format(channel) for channel in channels])


def format_state(state: bool) -> str:
    return 'ON' if state else 'OFF'


class HEPHY_BrandBox(Emulator):

    CHANNELS = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2']
    MODS = ['IV', 'CV']

    IDENTITY = 'BrandBox, v2.0 (Emulator)'
    SUCCESS = 'OK'
    COMMAND_ERROR = 'Err99'

    closed_channels: Set[str] = set()
    test_state = False
    mod = 'N/A'

    def __init__(self):
        super().__init__()

        self.add_route(r"^\*IDN\?$", lambda: self.IDENTITY)
        self.add_route(r"^\*RST$", lambda: self.SUCCESS)
        self.add_route(r"^\*CLS$", lambda: self.SUCCESS)
        self.add_route(r"^\*STB\?$", self.handle_stb)
        self.add_route(r"^\*STR\?$", lambda: "0")
        self.add_route(r"^\*OPC\?$", lambda: "1")
        self.add_route(r"^:CLOS (.+)$", self.handle_close)
        self.add_route(r"^:OPEN (.+)$", self.handle_open)
        self.add_route(r"^:CLOS:STAT\?$", self.handle_close_state)
        self.add_route(r"^:OPEN:STAT\?$", self.handle_open_state)
        self.add_route(r"^:DEBUG?$", lambda: self.COMMAND_ERROR)
        self.add_route(r"^SET:(A|B|C)_(ON|OFF)$", self.handle_set)
        self.add_route(r"^SET:(A1|A2|B1|B2|C1|C2)_(ON|OFF)$", self.handle_set_abc)
        self.add_route(r"^SET:MOD (IV|CV)$", self.handle_set_mod)
        self.add_route(r"^GET:(A|B|C) \?$", self.handle_get)
        self.add_route(r"^GET:(A1|A2|B1|B2|C1|C2) \?$", self.handle_get_abc)
        self.add_route(r"^GET:MOD \?$", self.handle_get_mod)
        self.add_route(r"^GET:TST \?$", self.handle_get_test)
        self.add_route(r"^SET:TST (ON|OFF)$", self.handle_set_test)
        self.add_route(r"^.*$", self.handle_unknown_message)

    @property
    def opened_channels(self):
        return set(self.CHANNELS) - self.closed_channels

    def handle_stb(self):
        states = []
        for channel in self.CHANNELS:
            states.append('1' if channel in self.closed_channels else '0')
        return ','.join(states)

    def handle_close(self, channels):
        for channel in split_channels(channels):
            if self.has_channel(channel):
                self.closed_channels.add(channel)
            else:
                return self.COMMAND_ERROR
        return self.SUCCESS

    def handle_open(self, channels):
        for channel in split_channels(channels):
            if self.has_channel(channel):
                if channel in self.closed_channels:
                    self.closed_channels.remove(channel)
            else:
                return self.COMMAND_ERROR
        return self.SUCCESS

    def handle_close_state(self):
        return join_channels(sorted(self.closed_channels))

    def handle_open_state(self):
        return join_channels(sorted(self.opened_channels))

    def handle_set(self, prefix, state):
        for channel in [f'{prefix}{index}' for index in [1, 2]]:
            if state == 'ON':
                self.closed_channels.add(channel)
            else:
                if channel in self.closed_channels:
                    self.closed_channels.remove(channel)
        return self.SUCCESS

    def handle_set_abc(self, channel, state):
        if state == 'ON':
            self.closed_channels.add(channel)
        else:
            if channel in self.closed_channels:
                self.closed_channels.remove(channel)
        return self.SUCCESS

    def handle_set_mod(self, mod):
        if mod not in self.MODS:
            return self.COMMAND_ERROR
        self.mod = mod
        return self.SUCCESS

    def handle_get(self, prefix):
        states = []
        for channel in [f'{prefix}{index}' for index in [1, 2]]:
            states.append(format_state(channel in self.closed_channels))
        return ','.join(states)

    def handle_get_abc(self, channel):
        return format_state(channel in self.closed_channels)

    def handle_get_mod(self):
        return format(self.mod)

    def handle_get_test(self):
        return format_state(self.test_state)

    def handle_set_test(self, value):
        self.test_state = value == 'ON'
        return self.SUCCESS

    def handle_unknown_message(self):
        return self.COMMAND_ERROR

    def has_channel(self, channel):
        return channel in self.CHANNELS
