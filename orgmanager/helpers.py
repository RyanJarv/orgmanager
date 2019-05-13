from os import path
from typing import TextIO, Dict, AnyStr, Any
from collections.abc import Sequence

from tabulate import tabulate


def format_print(output):
    if isinstance(output, str):
        print(output)
    elif isinstance(output, Sequence) and isinstance(output[1], dict):
        headers = list(map(str, output[0].keys()))
        data = [list(map(str, x.values())) for x in output]
        print(tabulate(data, headers=headers))
    elif isinstance(output, dict) and len(output.keys()) == 1:
        k = list(output.keys())[0]
        print('{0}:'.format(k))
        for k, v in iter(output[k].items()):
            print('\t{0}: {1}'.format(k, v))
        print('\n')
    else:
        print('Object not matched in format_print')
        print(str(output))

class safe_open:
    def __init__(self, fpath):
        self.fpath: str = fpath
        self.f: TextIO = None
    def __enter__(self):
        dir = path.dirname(self.fpath)
        if not path.exists(dir):
            path.mkdir(dir)
        self.f = open(self.fpath, 'x')
        return self.f
    def __exit__(self, type, value, traceback):
        self.f.close()
