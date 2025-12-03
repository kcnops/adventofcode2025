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

joltage_length = 12

def get_largest_index_and_digit(int_list: List[int]) -> (int, int):
    largest = 0
    largest_idx = None
    for idx, digit in enumerate(int_list):
        if digit > largest:
            largest = digit
            largest_idx = idx
    if largest_idx is None:
        raise ValueError('Did not find any battery above 0 or algorithm error.')
    return largest_idx, largest

total_joltage = 0
for line in lines:
    line = line.strip()
    len_line = len(line)
    line = [int(x) for x in line]
    print(line)
    print(f'len line: {len_line}')

    # largest_joltage = 0
    # for idx, battery in enumerate(line):
    #     for idx_2, battery_2 in enumerate(line[idx+1:]):
    #         # print(battery + ' ' + battery_2)
    #         joltage = int(battery + battery_2)
    #         if joltage > largest_joltage:
    #             largest_joltage = joltage
    # print(largest_joltage)
    # total_joltage += largest_joltage

    # largest_leading = 0
    # largest_leading_idx = None
    # for idx, battery in enumerate(line[:len(line) - 1]):
    #     if int(battery) > largest_leading:
    #         largest_leading = int(battery)
    #         largest_leading_idx = idx
    # # print(f'{largest_leading} @ {largest_leading_idx}')
    #
    # if largest_leading_idx is None:
    #     raise ValueError('Did not find any battery above 0 or algorithm error.')
    #
    # largest_trailing = 0
    # for battery in line[largest_leading_idx + 1:]:
    #     if int(battery) > largest_trailing:
    #         largest_trailing = int(battery)
    # # print(f'{largest_trailing}')
    #
    # total_joltage += 10 * largest_leading + largest_trailing

    joltage = 0
    next_idx = 0
    for i in range(joltage_length):
        # i is how many digits already found
        print(f'i: {i}')
        len_still_needed = len_line - joltage_length + i + 1
        print(f'len still needed: {len_still_needed}')
        line_to_look_in = line[next_idx:len_still_needed]
        print(line_to_look_in)
        relative_idx, largest = get_largest_index_and_digit(line_to_look_in)
        next_idx = next_idx + relative_idx + 1
        joltage = 10 * joltage + largest
        print(f'{joltage}')
    print(f'{joltage}')

    total_joltage += joltage

print(total_joltage)

# 169732779262668 is too high