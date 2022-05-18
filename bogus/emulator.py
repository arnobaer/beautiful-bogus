import re
from typing import Any, Callable, Dict, Iterable, Optional, Union

__all__ = ["Emulator"]


class Property:

    def __init__(self, default: Any, *, type: Callable = None, choice: Iterable = None, 
                 format: Union[str, Callable] = None) -> None:
        self.value: Any = default
        self.default: Any = default
        self.type: Callable = type
        self.choice = choice
        self.format: Union[str, Callable] = format
        
    def update(self, value: Any) -> None:
        if self.type is not None:
            value = self.type(value)
        if self.choice is not None:
            if value not in self.choice:
                raise ValueError(value)
        self.value = value
        
    def reset(self) -> None:
        self.value = self.default
        
    def __call__(self, *args):
        if not args:
            return format(self)
        return self.update(*args)
        
    def __str__(self):
        if self.format is None:
            return format(self.value)
        elif isinstance(self.format, str):
            return format(self.value, self.format)
        else:
            return self.format(self.value)


class Route:

    def __init__(self, route: str, target: Callable) -> None:
        self.route = route
        self.target = target
        
    def match(self, message: str) -> Optional[list]:
        m = re.match(self.route, message)
        if m is not None:
            return m.groups()
        return None


class Emulator:

    def __init__(self):
        self._routes: Dict[str, Route] = {}

    def add_route(self, route: str, target: Callable) -> None:
        if route in self._routes:
            raise KeyError(route)
        self._routes[route] = Route(route, target)

    def dispatch(self, message: str) -> Optional[str]:
        for route in self._routes.values():
            result = route.match(message)
            if result is not None:
                return route.target(*result)
        return result
        
