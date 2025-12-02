import os

input = os.path.join(os.path.dirname(__file__), 'input.txt')
with open(input) as f:
    lines = f.read().splitlines()


starting_pos = 50
pos = starting_pos
zero_count = 0
new_zero_count = 0
print('Staring at ', starting_pos)
for line in lines:
    direction = line[0]
    magnitude = int(line[1::])
    if direction == 'R':
        print(f'Moving right {magnitude} and landing at {pos+magnitude}')
        new_zero_count+= ((pos+magnitude)//100)
        print(f'Passes {((pos+magnitude)//100)} times through 0')
        pos = (pos + magnitude)%100
        print('Position ', pos)
    elif direction == 'L':
        print(f'Moving left {magnitude} and landing at {pos-magnitude}')
        if pos==0:
            new_zero_count+= magnitude//100
            print(f'Passes {magnitude//100} times through 0')
        else:
            new_zero_count+= ((magnitude + (100 - pos)) // 100)
            print(f'Passes {((magnitude + (100 - pos)) // 100)} times through 0')
        pos = (pos - magnitude)%100
        print('Position ', pos)

print('Total ', new_zero_count)
