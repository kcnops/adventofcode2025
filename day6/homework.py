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

ALL_OPERATORS = ['+', '*']

numbers: list[list[int]] = []
parsed_numbers = False
operators: List[str] = []

for line in lines:
    if parsed_numbers:
        # Currently ignore any operator line but first
        continue
    else:
        splitted = line.split(' ')
        if splitted[0].strip() in ALL_OPERATORS:
            parsed_numbers = True
            operators = [operator.strip() for operator in splitted if operator.strip() != '']
        else:
            numbers_line = []
            for possible_number in splitted:
                stripped_possible_number = possible_number.strip()
                if stripped_possible_number != '':
                    numbers_line.append(int(stripped_possible_number))
            numbers.append(numbers_line)

print(numbers)
print(operators)

n_calculations = len(operators)
print(f'n_calculation = {n_calculations}')
n_numbers = len(numbers)
print(f'n_numbers = {n_numbers}')

sum = 0
for i in range(n_calculations):
    print(f'Calulation {i}')
    operator = operators[i]
    solution = numbers[0][i]
    for j in range(1,n_numbers):
        if operator == '*':
            solution = solution * numbers[j][i]
        elif operator == '+':
            solution = solution + numbers[j][i]
        print(f'temp solution in calculation {i}: {solution}')
    print(solution)
    sum += solution

print(sum)