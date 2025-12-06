import os
import sympy as sp
import tqdm

input = os.path.join(os.path.dirname(__file__), 'input.txt')
with open(input) as f:
    lines = f.read().splitlines()
    
max_list = []
for bank in tqdm.tqdm(lines):
    max_string = ''
    start = 0
    for k in range(12):
        end = len(bank)-(12-k)
        best_i = start
        best_digit = bank[best_i]
        for i in range(start, end+1):
            digit = bank[i]
            if digit > best_digit:
                best_digit = digit
                best_i = i
        max_string+=best_digit
        start = best_i+1
    print(max_string)
    # max_list.append(int(max_string))
# print(max_list)
print(sum(max_list))