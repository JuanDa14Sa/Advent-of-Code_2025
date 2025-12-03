import os

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
    # print(f'Checking {id_range}')
    for number in id_range_list:
        number_str = str(number)
        # print(f'Cheking {number}')
        half_str = number_str[len(number_str)//2::]
        if len(number_str) % 2 == 1:
            pass
        else:
            pattern = number_str[:len(number_str)//2]
            if half_str == pattern:
                # print(f'Match found for {pattern} in {half_str}')
                match_counter+=1
                invalid_ids.append(number)
                invalid_ids_sum+=int(number)
                
    # print('-'*50)
print(f'Total matches {match_counter}')
print(f'Invalid ids {invalid_ids}')
print(f'Sum of invalid ids {invalid_ids_sum}')