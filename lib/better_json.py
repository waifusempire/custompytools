"""A new way to work with `.json` files."""

import sys
from types import NoneType
from typing import Iterable, Optional, Type, Union, final, Any, TypeVar
from io import TextIOWrapper
import json


if sys.version_info >= (3, 11):
    import typing
    Self = typing.Self
elif sys.version_info >= (3, 7) and sys.version_info <= (3, 10):
    import typing_extensions
    Self = typing_extensions.Self
else:
    import typing
    class _Self(typing._Final, _root=True):

        __slots__ = ()

        def __instancecheck__(self, obj):
            raise TypeError(f"{self} cannot be used with isinstance().")

        def __subclasscheck__(self, cls):
            raise TypeError(f"{self} cannot be used with issubclass().")

    Self = _Self


DEFAULT = TypeVar("DEFAULT")


LOADED = TypeVar(
    "LOADED", bound="JsonIO.is_marked")
DUMPED = TypeVar(
    "DUMPED", bound="JsonIO.is_marked")


class JsonObject(dict):
    """This is a subclass of `:class:dict`"""
    def __new__(cls: Type[Self], *args, **kwargs) -> Self:
        return super().__new__(cls, *args, **kwargs)

    def __init__(self: Self, **key_value: Optional[Union[int, float, bool, str, dict, list, tuple]]):
        """Acceptable Values
=================\n
`'1': bool -> json boolean`\n
`'2': str -> json string`\n
`'3': int | float -> json number`\n
`'4': JsonObject | dict -> json object`\n
`'5': JsonArray | list | tuple -> json array`\n
`'6': None -> json null`
"""
        if not len(key_value) == 0:
            for i, j in key_value.items():
                if isinstance(j, (int, str, float, dict, list, tuple, NoneType, bool, type(self), JsonArray)):
                    pass
                else:
                    raise TypeError(f"'{j}' is not of a valid json type")
        else:
            pass
        super().__init__(**key_value)

    @classmethod
    def from_dict(cls: Type[Self], _dict: dict, /) -> Self:
        return cls(**_dict)

    def remove(self, key: str):
        super().pop(key)

    def get(self, key: str, default: Optional[Any] = DEFAULT) -> Any | None:
        if default == DEFAULT:
            return super().get(key)
        else:
            return super().get(key, default)

    def clear(self) -> None:
        return super().clear()

    def items(self) -> Any:
        return super().items()

    def copy(self):
        return type(self)(**self)


class JsonArray(list):
    """This a subclass of `:class:list`"""
    def __new__(cls: Type[Self], *args) -> Self:
        return super().__new__(cls)

    def __init__(self: Self, *args: Optional[Union[int, float, bool, str, dict, list, tuple]]) -> None:
        """Acceptable Values
=================\n
`'1': bool -> json boolean`\n
`'2': str -> json string`\n
`'3': int | float -> json number`\n
`'4': JsonObject | dict -> json object`\n
`'5': JsonArray | list | tuple -> json array`\n
`'6': None -> json null`
"""
        super().__init__(args)

    def add(self, object: Optional[object], index: int = DEFAULT):
        if index == DEFAULT:
            super().append(object)
        else:
            super().insert(index, object)

    def remove(self, index: int):
        super().pop(index)

    def get(self, index: int):
        return self[index]

    def copy(self):
        return type(self)(*self)

    @classmethod
    def from_iterable(cls: Type[Self], iterable: Iterable) -> Self:
        return cls(*list(iterable))


Json_Object_or_Array = Union[JsonArray, JsonObject, dict, list, tuple]


MODE = "mode"
FILE = "file"
NAME = "name"


@final
class JsonIO:

    def __init__(self, **__data) -> None:
        __data["loaded"] = False
        __data["dumped"] = False
        self.__data__ = __data

    def load(self, **kwargs) -> Union[dict, list]:
        if self.mode == "d":
            raise Exception("Undefined load method with mode 'd'")
        else:
            if self.is_marked_loaded:
                raise Exception(
                    "Unable to load file\nFile is already marked as Loaded")
            else:
                self.__data__["loaded"] = True

                data = json.load(self.file, **kwargs)
                if isinstance(data, dict):
                    return JsonObject(**data)
                elif isinstance(data, list):
                    return JsonArray(*data)
                else:
                    print(type(data))

    def dump(self, data: Union[list, dict, tuple], **kwargs) -> None:
        if self.mode == "l":
            raise Exception("Undefined dump method with mode 'l'")
        else:
            if self.is_marked_dumped:
                raise Exception(
                    "Unable to dump to file\nFile is already marked as Dumped")
            else:
                self.__data__["dumped"] = True
                json.dump(data, self.file, **kwargs)

    def __repr__(self) -> str:
        return f"<JsonIO(file='{self.name}' mode='{self.mode}')>"

    @property
    def closed(self) -> bool:
        return self.file.closed

    @property
    def name(self) -> str:
        return self.file.name if self.file else self._data[NAME]

    @property
    def file(self) -> TextIOWrapper:
        return self._data[FILE]

    @property
    def mode(self) -> str:
        return self._data[MODE]

    def _is_marked(self, _as: LOADED | DUMPED, /) -> bool:
        if _as == LOADED:
            return self._data["loaded"]
        elif _as == DUMPED:
            return self._data["dumped"]
        else:
            raise ValueError(
                "Invalid value, _as may only be 'DUMPED' or 'LOADED'")

    @property
    def is_marked_loaded(self):
        return self._is_marked(LOADED)

    @property
    def is_marked_dumped(self):
        return self._is_marked(DUMPED)

    def __init_subclass__(cls) -> None:
        raise Exception(
                f"Base class \"{cls.__name__}\" is marked final and cannot be subclassed")

class OpenJson:

    def __init__(self, file_name: str, mode: str = "l"):
        """Parameters
        =========\n
        file_name: `str`\n
        mode: `str` = `'l'` | `'d'`\n
        Description - `l - load`, `d - dump`"""
        file_name = file_name if not file_name.endswith(
            ".json") else file_name.split(".json")[0]

        class InvalidMode(Exception):
            def __init__(self, *args: object) -> None:
                super().__init__(*args)

        if mode == "l":
            file = open(f"{file_name}.json", "r")
        elif mode == "d":
            file = open(f"{file_name}.json", "w")
        else:
            raise InvalidMode(f"'{mode}' is not a valid mode!")
        self.__data__: dict[str, Any] = dict(
            mode=mode, file_name=file_name, file=file)

    def __enter__(self):
        return JsonIO(file=self.__data__[FILE], mode=self.__data__[MODE], name=self.__data__["file_name"]+".json")

    def __exit__(self, *args):
        self.__data__['file'].close()

    def __repr__(self) -> str:

        FILE_NAME = "file_name"
        return f"<Json(file_name={self.__data__[FILE].name if self.__data__[FILE] else f'{self.__data__[FILE_NAME]}.json'}, mode={self.__data__[MODE]})>"


class StringJson:
    load = json.loads
    dump = json.dumps


__all__ = (OpenJson.__name__, DUMPED.__name__, LOADED.__name__,
           JsonArray.__name__, JsonObject.__name__, StringJson.__name__)
