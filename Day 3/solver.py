import os
import sympy as sp
import tqdm

input = os.path.join(os.path.dirname(__file__), 'input.txt')
with open(input) as f:
    lines = f.read().splitlines()
    
max_list = []
for bank in tqdm.tqdm(lines):
    max_pair = '00'
    for i in range(len(bank)):
        for j in range(i+1, len(bank)):
            max_pair = max(int(max_pair), int(bank[i]+bank[j]))
    max_list.append(max_pair)
print(max_list)
print(sum(max_list))