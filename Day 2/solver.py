import os
import sympy as sp
import tqdm

input = os.path.join(os.path.dirname(__file__), 'input.txt')
with open(input) as f:
    lines = f.read().splitlines()
list_ids = []
for line in lines:
    list_ids.append(line.split(','))

match_counter = 0
invalid_ids = []
for id_range in tqdm.tqdm(list_ids[0], desc="Processing ranges"):
    start = int(id_range.split('-')[0])
    end = int(id_range.split('-')[1])
    id_range_list = range(start, end+1)
    # print(f'Checking {id_range}')
    for number in id_range_list:
        number_str = str(number)
        # print(f'Cheking {number}')
        if sp.isprime(len(number_str)):
            pattern_str = number_str[0]
            all_match = True
            for digit in number_str[1:]:
                if digit != pattern_str:
                    all_match = False
                    break
            if all_match:
                # print("Match found")
                invalid_ids.append(number)
                match_counter += 1
        else:
            divisors = sp.proper_divisors(len(number_str))
            for divisor in divisors:
                pattern_str = number_str[:divisor]
                times = len(number_str)//divisor
                if pattern_str * times == number_str:
                    # print('Match found')
                    invalid_ids.append(number)
                    match_counter+=1
                    break

print(f'Total matches {match_counter}')
print(f'Invalid ids {invalid_ids}')
print(f'Sum of invalid ids {sum(invalid_ids)}')