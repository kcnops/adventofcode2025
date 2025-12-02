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
    line = file.readline().strip()

ranges = line.split(',')

invalid_sum = 0
for test_range in ranges:
    edges = test_range.split('-')
    from_edge = int(edges[0])
    to_edge = int(edges[1])

    for i in range(from_edge, to_edge+1):
        i_str = str(i)
        # print(f'Testing {i_str}')

        # PART 1
        # if len(i_str) % 2 == 1:
        #     # odd length numbers can't be invalid
        #     continue
        # i_len = len(i_str)
        # half_len = int(i_len/2)
        # if i_str[0:half_len] == i_str[half_len:]:
        #     print(f'Invalid code found: {i}')
        #     invalid_sum += i

        # PART 2
        i_len = len(i_str)
        half_len = int(i_len / 2)
        for i_test_len in range(1, half_len+1):
            if i_len % i_test_len != 0:
                # length of i not dividable by test length so skip
                continue
            times = int(i_len / i_test_len)
            invalid = True
            initial_i_part = i_str[0:i_test_len]
            for time in range(1,times):
                test_i_part = i_str[time*i_test_len:(time+1)*i_test_len]
                if test_i_part != initial_i_part:
                    invalid = False
                    continue

            if invalid:
                print(f'Invalid code found: {i} with repeating {initial_i_part}')
                invalid_sum += i
                break

print(invalid_sum)

