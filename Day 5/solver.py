import os 


input = os.path.join(os.path.dirname(__file__), 'input.txt')
with open(input) as f:
    lines = f.read().strip()
blocks = lines.split('\n\n')

fresh_ingredients = blocks[0].splitlines()
available_ingredients = blocks[1].splitlines()

# print(fresh_ingredients)
# print(available_ingredients)    
fresh_available_ingredients = []

min_start = 0
ranges =[]
for fresh_ingredient_range in fresh_ingredients:
    start, end = int(fresh_ingredient_range.split('-')[0]), int(fresh_ingredient_range.split('-')[1])
    ranges.append((start, end))
    
ranges.sort(key=lambda x:x[0])

merged = []

for range in ranges:
    if not merged:
        merged.append(range)
    else:
        last_start, last_end = merged[-1]
        current_start, current_end = range
        if current_start <= last_end:
            merged[-1] = (last_start, max(last_end, current_end))
        else: 
            merged.append(range)

total_size = sum(end - start + 1 for start, end in merged)
print(total_size)
        