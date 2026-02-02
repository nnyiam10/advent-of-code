from pathlib import Path
from typing import Union

PathLike = Union[str, Path]

def read_lines(filename: PathLike):
    path = Path(filename)
    with path.open() as f:
        return [line.strip() for line in f]

def read_lines_raw(filename: PathLike):
    path = Path(filename)
    with path.open() as f:
        return [line for line in f]

def read_raw(filename: PathLike):
    path = Path(filename)
    with path.open() as f:
        return f.read().strip()

def read_grid_from_file(filename: PathLike):
    path = Path(filename)
    with path.open() as f:
        return [[int(char) for char in line.strip()] for line in f]

def read_text_grid_from_file(filename: PathLike):
    path = Path(filename)
    with path.open() as f:
        return [[char for char in line.strip('\n')] for line in f]

def read_text_grid_from_file_with_split(filename: PathLike):
    path = Path(filename)
    with path.open() as f:
        return [line.split() for line in f]