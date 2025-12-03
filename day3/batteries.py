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

total_joltage = 0
for line in lines:
    line = line.strip()
    print(line)

    # largest_joltage = 0
    # for idx, battery in enumerate(line):
    #     for idx_2, battery_2 in enumerate(line[idx+1:]):
    #         # print(battery + ' ' + battery_2)
    #         joltage = int(battery + battery_2)
    #         if joltage > largest_joltage:
    #             largest_joltage = joltage
    # print(largest_joltage)
    # total_joltage += largest_joltage

    largest_leading = 0
    largest_leading_idx = None
    for idx, battery in enumerate(line[:len(line)-1]):
        if int(battery) > largest_leading:
            largest_leading = int(battery)
            largest_leading_idx = idx
    # print(f'{largest_leading} @ {largest_leading_idx}')

    if largest_leading_idx is None:
        raise ValueError('Did not find any battery above 0 or algorithm error.')

    largest_trailing = 0
    for battery in line[largest_leading_idx+1:]:
        if int(battery) > largest_trailing:
            largest_trailing = int(battery)
    # print(f'{largest_trailing}')

    total_joltage += 10*largest_leading + largest_trailing

print(total_joltage)