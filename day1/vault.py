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

vault_position = 50

at_zero = 0
passed_zero = 0
for line in lines:
    line = line.strip()
    print(line)
    direction = line[0]
    moves = int(line[1:])

    at_zero_now = 0

    # TRY 1
    # if direction == 'L':
    #     new_vault_position = (vault_position - moves)
    # elif direction == 'R':
    #     new_vault_position = (vault_position + moves)
    # else:
    #     print(f'ERROR: Unknown move direction {direction}')
    #
    # print(new_vault_position)
    # if new_vault_position % 100 == 0:
    #     at_zero += 1
    #     print('AT ZERO!')
    # if vault_position != 0 and new_vault_position < 0 or new_vault_position > 100:
    #     passed_zero += 1
    #     print('PASSED ZERO')
    # vault_position = new_vault_position % 100
    # print(f'corrected to {vault_position}')

    # TRY 2
    # for i in range(moves):
    #     if direction == 'L':
    #         vault_position = (vault_position - 1)
    #         if vault_position < 0:
    #             print('ZERO')
    #             at_zero += 1
    #             vault_position += 100
    #     elif direction == 'R':
    #         vault_position = (vault_position + 1)
    #         if vault_position >= 100:
    #             print('ZERO')
    #             at_zero += 1
    #             vault_position -= 100
    #     else:
    #         print(f'ERROR: Unknown move direction {direction}')
    # print(vault_position)

    # TRY 3
    # if direction == 'L':
    #     new_vault_position = (vault_position - moves)
    # elif direction == 'R':
    #     new_vault_position = (vault_position + moves)
    # else:
    #     print(f'ERROR: Unknown move direction {direction}')
    #
    # print(new_vault_position)
    #
    # if new_vault_position % 100 == 0:
    #     print('AT ZERO!')
    #     at_zero += 1
    #     at_zero_now = 1
    #
    # result = new_vault_position // 100
    # if vault_position != 0 and result != 0:
    #     print(f'PASSED ZERO: {result}')
    #     passed_zero += abs(result) - at_zero_now
    #
    # vault_position = new_vault_position % 100
    # print(f'corrected to {vault_position}')

print(f'At zero: {at_zero}x & passed zero: {passed_zero}x, total: {at_zero + passed_zero}')

# Try 1 2654 too low
# Try 2 6272 too high
# Try 3 5102 too low
