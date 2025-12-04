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

grid = [line.strip() for line in lines]

# returns amount of rolls reaches & removed
def remove_rolls(local_grid: list[str]) -> (int, list[str]):
    max_r = len(local_grid)
    max_c = len(local_grid[0])
    reachable_rolls = 0
    new_grid = []
    for r, row in enumerate(local_grid):
        new_row = []
        for c, possible_roll_char in enumerate(row):
            # Not a paper (empty or already removed), so don't do anything, just append existing
            if possible_roll_char != '@':
                new_row.append(possible_roll_char)
                continue
            papers_around = 0
            # print(f'checking {r}-{c}')
            # left up
            if r > 0 and c > 0 and local_grid[r - 1][c - 1] == '@':
                papers_around += 1
            # up
            if r > 0 and local_grid[r - 1][c] == '@':
                papers_around += 1
            # right up
            if r > 0 and c < max_c - 1 and local_grid[r - 1][c + 1] == '@':
                papers_around += 1
            # left
            if c > 0 and local_grid[r][c - 1] == '@':
                papers_around += 1
            # right
            if papers_around < 4 and c < max_c - 1 and local_grid[r][c + 1] == '@':
                papers_around += 1
            # left down
            if papers_around < 4 and r < max_r - 1 and c > 0 and local_grid[r + 1][c - 1] == '@':
                papers_around += 1
            # down
            if papers_around < 4 and r < max_r - 1 and local_grid[r + 1][c] == '@':
                papers_around += 1
            # right down
            if papers_around < 4 and r < max_r - 1 and c < max_c - 1 and local_grid[r + 1][c + 1] == '@':
                papers_around += 1
            # if reachable: counter++ and replace @ by x
            if papers_around < 4:
                reachable_rolls += 1
                new_row.append('x')
                # print('reachable roll found')
            # if not reachable: keep @
            else:
                new_row.append('@')
        new_grid.append(new_row)
    return reachable_rolls, new_grid

# reachable_rolls, new_grid = remove_rolls(lines)
# print(reachable_rolls)

total_rolls_removed = 0
changed = True
while(changed):
    rolls_removed, new_grid = remove_rolls(grid)
    total_rolls_removed += rolls_removed
    if new_grid == grid:
        print('Grid unchanged, quitting')
        changed = False
    else:
        print('Grid changed, continuing')
        grid = new_grid
print(total_rolls_removed)
