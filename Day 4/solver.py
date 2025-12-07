import os
import tqdm
import copy

input = os.path.join(os.path.dirname(__file__), 'input.txt')
with open(input) as f:
    lines = f.read().splitlines()
    
grid_charts = [list(line) for line in lines]
grid = [[str(ch) for ch in line] for line in lines]    

directions = [
    (-1, -1), (-1, 0), (-1, 1),
    ( 0, -1),         ( 0, 1),
    ( 1, -1), ( 1, 0), ( 1, 1)
]

rows = len(grid)
cols = len(grid[0])
new_accesibles = True
iteration = 0
total_accesibles = 0

while new_accesibles:
    grid_copy = copy.deepcopy(grid)
    accesible_count = 0
    for i in range(rows):
        for j in range(cols):
            current_cell = grid[i][j]
            paper_rolls_count = 0
            if current_cell == '@':
                for dh, dv in directions:
                    new_row_pos, new_col_pos = i + dh, j + dv
                    if 0 <= new_row_pos < rows and 0 <= new_col_pos < cols:
                        neighbor = grid[new_row_pos][new_col_pos]
                        # print(f"Neighbor: {neighbor}\tPosition: {new_row_pos, new_col_pos}")
                        if neighbor == '@':
                            paper_rolls_count += 1

                if paper_rolls_count < 4:
                    # print('Accesible')
                    grid_copy[i][j] = 'x'
                    accesible_count += 1
                # print('-' * 50)
    
    total_accesibles+=accesible_count
    if accesible_count==0:
        new_accesibles=False
    grid = copy.deepcopy(grid_copy)  
    iteration+=1
    print(f'Iteration {iteration}\tAccesible count {accesible_count}\tTotal accesible {total_accesibles}')

 
# for i in range(rows):
#     print(grid_copy[i])
# print(f' Number of accesible rolls: {accesible_count}')
                
            