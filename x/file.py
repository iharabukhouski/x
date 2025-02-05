class file:

    def read(
        file,
    ):

        with open(file, 'r') as f:

            return f.read()

    def write(
        file,
        data,
    ):

        with open(file, 'w') as f:

            return f.write(data)
