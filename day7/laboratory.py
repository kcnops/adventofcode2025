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
        cols_with_times = {idx: 1}
        cols.add(idx)

if len(cols) == 0:
    raise ValueError('Did not find S on top row.')

splits = 0

row += 2
while row < depth:
    new_cols_with_times = {}
    for col, times in cols_with_times.items():
        if lines[row][col] == '^':
            print('split')
            splits += 1
            new_cols_with_times[col-1] = new_cols_with_times.get(col-1,0) + cols_with_times[col]
            new_cols_with_times[col+1] = new_cols_with_times.get(col+1,0) + cols_with_times[col]
        if lines[row][col] == '.':
            new_cols_with_times[col] = new_cols_with_times.get(col,0) + cols_with_times[col]
    cols_with_times = new_cols_with_times
    row += 2

print(splits)
# print(new_cols_with_times)
print(sum(new_cols_with_times.values()))