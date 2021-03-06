"""A new way to work with `.json` files."""

import sys
from typing import Any, Iterable, Optional, Type, Union, final
from io import TextIOWrapper
from typing import TypeVar
if sys.version_info >= 3.11:
    from typing import Self
else:
    from typing_extensions import Self


# TODO Create seperate classes for JsonIn and JsonOut


LOADED = TypeVar("LOADED", bound="JsonIO.is_marked")
DUMPED = TypeVar("DUMPED", bound="JsonIO.is_marked")


class JsonObject:
    def get(self: Self, key: str, default: Any = ...) -> Optional[Any} ...
    def remove(self: Self, key: str) -> None: ...
    def clear(self: Self) -> None: ...
    def items(self: Self) -> Any: ...
    def copy(self: Self) -> Self: ...
    @classmethod
    def from_dict(cls: Type[Self], _dict: dict) -> Self: ...
    def __new__(cls: Type[Self], *args, **kwargs) -> Self: ...
    def __init__(self: Self, **key_value: Optional[Union[int , float , bool , str ,
                 JsonObject , dict , JsonArray , list , tuple]]) -> None: ...


class JsonArray:
    def add(self: Self, object: Optional[object],
            index: int = ...) -> None: ...

    @classmethod
    def from_iterable(cls: Type[Self], iterable: Iterable) -> Self: ...
    def remove(self: Self, index: int) -> None: ...
    def get(self: Self, index: int) -> Any: ...
    def copy(self: Self) -> Self: ...
    def __new__(cls: Type[Self], *args) -> Self: ...
    def __init__(self: Self, *args: Optional[Union[int , float , bool , str ,
                 JsonObject , dict , JsonArray , list , tuple]]) -> None: ...


DictLike = TypeVar("DictLike", dict, JsonObject)
ListLike = TypeVar("ListLike", list, JsonArray, tuple)
Json_Object_or_Array = Union[JsonArray, JsonObject, dict, list, tuple]


@final
class JsonIO:
    def load(self, **kwargs) -> Union[JsonArray, JsonObject]: ...
    def dump(self, data: Union[DictLike, ListLike], **kwargs) -> None: ...
    @property
    def is_marked_loaded(self) -> bool: ...
    @property
    def is_marked_dumped(self) -> bool: ...
    @property
    def closed(self) -> bool: ...
    @property
    def name(self) -> str: ...
    @property
    def file(self) -> TextIOWrapper: ...
    @property
    def mode(self) -> str: ...
    def __init__(self, **__data) -> None: ...
    def __repr__(self) -> str: ...


class OpenJson:
    def __init__(self, file_name: str, mode: str = "l") -> None: ...
    def __enter__(self) -> JsonIO: ...
    def __exit__(self, *args) -> None: ...
    def __repr__(self) -> str: ...


class StringJson:
    def __init__(self) -> None: ...
    @staticmethod
    def load(json_string: str, **kwargs) -> dict | list: ...
    @staticmethod
    def dump(json_writable: Json_Object_or_Array, **kwargs) -> str: ...


__all__ = (OpenJson.__name__, DUMPED.__name__, LOADED.__name__,
           JsonArray.__name__, JsonObject.__name__, StringJson.__name__)
