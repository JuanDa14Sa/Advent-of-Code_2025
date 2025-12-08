import os 


input = os.path.join(os.path.dirname(__file__), 'input.txt')
with open(input) as f:
    lines = f.read().strip()
blocks = lines.split('\n\n')

fresh_ingredients = blocks[0].splitlines()
available_ingredients = blocks[1].splitlines()

print(fresh_ingredients)
print(available_ingredients)    
fresh_available_ingredients = set([])
for available_ingredient in available_ingredients:
    for fresh_ingredient_range in fresh_ingredients:
        start, end = int(fresh_ingredient_range.split('-')[0]), int(fresh_ingredient_range.split('-')[1])
        if int(available_ingredient)-start>=0 and int(available_ingredient)-end<=0:
            print(f'Ingredient {available_ingredient} is fresh')
            fresh_available_ingredients.add(available_ingredient)
print(fresh_available_ingredients)
print(len(fresh_available_ingredients))