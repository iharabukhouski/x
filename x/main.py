import os
import pandas as pd
from .file import read

def process(
    path,
    fn,
):

    files = os.listdir(f'{path}/raw')

    for file in files:

        raw = read(file)

        fn(
            file,
            raw
        )

def save(
    path,
    data,
):

    df = pd.DataFrame(data)

    os.makedirs(
        os.path.dirname(path),
        exist_ok=True
    )

    df.to_csv(path, index=False)
