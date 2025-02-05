import builtins
import time
from .env import env as _env
from .date import date as _date
from .file import file as _file

env = _env
date = _date
file = _file


_input = input


class range:

    def __init__(self):

        self.i = 0

    def __iter__(self):

        return self

    def __next__(self):

        return self.i


def _log(*args, **kvargs):

    print(*args, **kvargs)


builtins.log = _log


def _sleep(
    seconds=10000
):

    time.sleep(seconds)


builtins.sleep = _sleep


def _input(
    str,
):

    return _input(f'{str} ')


builtins.input = _input
