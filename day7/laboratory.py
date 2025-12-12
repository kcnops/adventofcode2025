import itertools
import math
import os
from dataclasses import dataclass
from multiprocessing import Process, Pool
from pathlib import Path
from typing import List, Optional
from tqdm import tqdm
import copy
import time
import re

cwd = os.getcwd()

this_dir = Path(__file__).parent
input_file = this_dir / 'input.txt'

with input_file.open('r') as file:
    lines = file.readlines()

lines = [line.strip() for line in lines]

depth = len(lines)
width = len(lines[0])

row = 0
cols = set()
for idx, place in enumerate(lines[row]):
    if place == 'S':
        cols.add(idx)

if len(cols) == 0:
    raise ValueError('Did not find S on top row.')

splits = 0

row += 2
while row < depth:
    new_cols = set()
    for col in cols:
        if lines[row][col] == '^':
            print('split')
            splits += 1
            new_cols.add(col-1)
            new_cols.add(col+1)
        if lines[row][col] == '.':
            new_cols.add(col)
    cols = new_cols
    row += 2

print(splits)