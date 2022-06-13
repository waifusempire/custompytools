from dataclasses import dataclass
import os
import subprocess
from typing import IO, Any, TypeVar


CMD = TypeVar("CMD", str, str)
FILE = TypeVar("FILE", None, int, IO)


@dataclass
class Completed:
    process: Any
    returncode: int
    stderr: Any = None
    stdout: Any = None
    args: Any = None





class OSSystemCompleted(object):
    def __new__(cls, __code, __command, *args):
        new = super().__new__(cls)
        new.__dict__.update(code=__code, cmd=__command, randargs=args)
        return new

    @property
    def returncode(self) -> int:
        return self.__dict__.get("code")

    @property
    def command(self) -> str:
        return self.__dict__.get("cmd")

    def __repr__(self) -> str:
        return f"OSSystemCompleted({self.returncode}, '{self.command}')"


def execute_command(command: CMD | str, text: bool = True, stdout: FILE = subprocess.PIPE, stdin: FILE = subprocess.PIPE, stderr: FILE = subprocess.PIPE):
    "Tries executing command with `subprocess.run` on case of failure it tries to execute command with `os.system`"
    try:
        a = subprocess.run(command.split(" "), text=text, stdin=stdin, stdout=stdout, stderr=stderr)
        return Completed(a, a.returncode, a.stderr, a.stdout, a.args)
    except FileNotFoundError as error:
        a = OSSystemCompleted(os.system(command), command, error)
        return Completed(a, a.returncode, args=a.command)