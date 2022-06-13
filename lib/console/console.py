"""Simple console"""


from typing import overload
from .write import *
from .mode import *
from .read import *
from .flush import *
from .clear import *
from .execute import *


def console(mode: Mode, /,*args, **kwargs):
    """mode can only be of these types:\n
`Mode.write` | `W`\n
`Mode.read` | `R`\n
`Mode.clear` | `C`\n
`Mode.flush` | `F`\n
`Mode.execute` | `E`"""

    if mode == Mode.write:
        return write(*args, **kwargs)

    elif mode == Mode.read:
        try:
            return read(str(kwargs.get("_output", args[0])))
        except IndexError:
            return read(str(kwargs.get("_output", "")))

    elif mode == Mode.clear:
        return clear()

    elif mode == Mode.flush:
        return flush()

    elif mode == Mode.execute:
        return execute_command(*args, **kwargs)

    else:
        raise InvalidModeState(mode)


class Console:
    write = write
    clear = clear
    read = read
    flush = flush
    execute = execute_command
