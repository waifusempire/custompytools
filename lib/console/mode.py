"""Simple Mode class"""


from enum import Enum
from random import randint


class Mode(Enum):
    write = randint(0, 9999)
    read = randint(10000, 19999)
    clear = randint(20000, 29999)
    flush = randint(30000, 39999)
    execute = randint(40000, 49999)


R = Mode.read
W = Mode.write
C = Mode.clear
F = Mode.flush
E = Mode.execute


InvalidMode = object


class InvalidModeState(Exception):
    def __init__(self, m: InvalidMode) -> None:
        super().__init__(f"'{m}' is not a valid mode!")
        self.invalid_mode = m