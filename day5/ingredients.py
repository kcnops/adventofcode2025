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

ranges: list[tuple[int,int]] = []
parsed_ranges = False
ingredients: List[int] = []
lowsest_range_id = 9999999999999999999999999999999
highest_range_id = 0

for line in lines:
    if parsed_ranges:
        ingredients.append(int(line))
    else:
        if line == '':
            parsed_ranges = True
        else:
            splitted = line.split('-')
            ranges.append((int(splitted[0]),int(splitted[1])))
            if int(splitted[0]) < lowsest_range_id:
                lowsest_range_id = int(splitted[0])
            if int(splitted[1]) > highest_range_id:
                highest_range_id = int(splitted[1])

print(ranges)
print(ingredients)

if lowsest_range_id > highest_range_id:
    raise ValueError('lowest found id > highest found id ...')

# good_ingredients = 0
# for ingredient in ingredients:
#     for range in ranges:
#         if ingredient < range[0]:
#             continue
#         if ingredient > range[1]:
#             continue
#         good_ingredients += 1
#         print(f'{ingredient} is good')
#         break
#
# print(good_ingredients)

possible_good_ingredients = 0

for ingredient in tqdm(range(lowsest_range_id, highest_range_id + 1)):
    for range in ranges:
            if ingredient < range[0]:
                continue
            if ingredient > range[1]:
                continue
            possible_good_ingredients += 1
            # print(f'{ingredient} would be good')
            break

