"""Simple read function"""
from typing import Union, overload


@overload
def read() -> str: ...


@overload
def read(_type=bool) -> bool: ...


@overload
def read(_type=int) -> int: ...


@overload
def read(_type=float) -> float: ...


@overload
def read(_type=str) -> str: ...


@overload
def read(_output: str) -> str: ...


@overload
def read(_output: str, _type=bool) -> bool: ...


@overload
def read(_output: str, _type=int) -> int: ...


@overload
def read(_output: str, _type=float) -> float: ...


@overload
def read(_output: str, _type=str) -> str: ...


def read(_output: str = "", _type: Union[str, int, float, bool] = str):
    history = input(_output)
    if _type == bool:
        if history.lower() == "true" or history == "1":
            return True
        elif history.lower() == "false" or history == "0":
            return False
    else:
        try:
            return _type(history)
        except Exception as a:
            raise a
