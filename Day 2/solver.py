import os

input = os.path.join(os.path.dirname(__file__), 'input.txt')
with open(input) as f:
    lines = f.read().splitlines()
list_ids = []
for line in lines:
    list_ids.append(line.split(','))

for id_range in list_ids[0]:
    start = int(id_range.split('-')[0])
    end = int(id_range.split('-')[1])
    id_range_list = range(start, end+1)
    print(f'Checking {id_range}')
    for number in id_range_list:  
        print(f'Cheking {number}')
        number_str = str(number)
        tmp_str= number_str[0]
        for i, digit in enumerate(number_str[1:]):
            print(f'Searching {tmp_str}')
            if tmp_str == number_str[i+1:i+len(tmp_str)+1]:
                print(f'Found {tmp_str}')
            else:
                tmp_str+=number_str[i+1]
                print(tmp_str)
                
    print('-'*50)