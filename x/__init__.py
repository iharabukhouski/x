import time
from .env import env as _env
from .date import date as _date
from .file import file as _file

env = _env
date = _date
file = _file


def sleep(
    seconds=10000,
):

    time.sleep(seconds)


_input = input


def input(
    str,
):

    return _input(f'{str} ')


class range:

    def __init__(self):

        self.i = 0

    def __iter__(self):

        return self

    def __next__(self):

        return self.i
