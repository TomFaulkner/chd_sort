#!/usr/bin/env python3

import os
import pathlib
import re

from contextlib import suppress

disc_pattern = re.compile("(.*?)(\(Disc\s\w\))")


def base_name(fn: str) -> str:
    match = re.search(disc_pattern, fn)
    if not match:
        raise Exception(f"No Disc in {fn}")
    return match.groups()[0].strip()


disc = '(Disc '


def handle_file(fn: str):
    base = base_name(fn) if disc in fn else fn.strip('.chd').strip()
    with suppress(FileExistsError):
        os.mkdir(base)
    os.rename(fn, os.path.join(base, fn))
    print(base)


if __name__ == '__main__':
    p = pathlib.Path('.')
    for fn in p.glob('*.chd'):
        handle_file(str(fn))
