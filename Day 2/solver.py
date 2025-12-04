import os
from primePy import primes

input = os.path.join(os.path.dirname(__file__), 'input.txt')
with open(input) as f:
    lines = f.read().splitlines()
list_ids = []
for line in lines:
    list_ids.append(line.split(','))

match_counter = 0
invalid_ids = []
invalid_ids_sum = 0
for id_range in list_ids[0]:
    start = int(id_range.split('-')[0])
    end = int(id_range.split('-')[1])
    id_range_list = range(start, end+1)
    print(f'Checking {id_range}')
    for number in id_range_list:
        number_str = str(number)
        print(f'Cheking {number}')
        if primes.check(len(number_str)):
            pattern_str = number_str[0]
            all_match = True
            for digit in number_str[1:]:
                if digit != pattern_str:
                    all_match = False
                    break
            if all_match:
                print("Match found")
                match_counter += 1
        # else:
        #     pattern_str = number_str[0]
        #     for digit in number_str[1:]:
        #         print(f'Using pattern {pattern_str}')
        #         if digit == pattern_str:
        #             print(f'Match found')
        #             match_counter+=1
        #         else:
        #             pattern_str+=digit
            
                
    # print('-'*50)

print(f'Total matches {match_counter}')
print(f'Invalid ids {invalid_ids}')
print(f'Sum of invalid ids {invalid_ids_sum}')