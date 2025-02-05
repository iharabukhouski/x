import os


class env:

    def get(
        key,
    ):

        return os.environ.get(key)
