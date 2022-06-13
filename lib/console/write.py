"""Simple write function"""
from typing import overload


@overload
def write() -> None: ...


@overload
def write(*_values) -> None: ...


@overload
def write(*_values, _sep: str) -> None: ...


@overload
def write(*_values, _end: str) -> None: ...


@overload
def write(*_values, _sep: str, _end: str) -> None: ...


def write(*_values, _sep: str = " ", _end: str = "\n"):
    import sys
    try:
        _writable_str = _sep.join(
            [str(i) for i in _values]) if len(_values) != 0 else ""
        sys.stdout.write(_writable_str)
    finally:
        sys.stdout.write(_end)