from copy import deepcopy

with open("input.txt", 'r') as f:
    lines = [list(row) for row in [line.strip() for line in f.readlines() if len(line) > 0]]

def shuffle_left_row(row):
    fall_index = 0
    for i in range(len(row)):
        if row[i] == '#':
            fall_index = i+1
        elif row[i] == 'O':
            row[i] = '.'
            row[fall_index] = 'O'
            fall_index += 1

    return row

def shuffle_grid_left(grid):
    new_grid = []
    for row in grid:
        new_grid.append(shuffle_left_row(row))

    return new_grid

def shuffle(dir, grid):
    """
    0 = up
    1 = right
    2 = down
    3 = left
    """
    if dir == 0:
        to_shuffle = []
        for i in range(len(grid[0])):
            to_shuffle.append([row[i] for row in grid])
        turned_shuffled = shuffle_grid_left(to_shuffle)
        shuffled = []
        for i in range(len(grid)):
            shuffled.append([row[i] for row in turned_shuffled])
    elif dir == 1:
        to_shuffle = [row[::-1] for row in grid]
        shuffled = [row[::-1] for row in shuffle_grid_left(to_shuffle)]
    elif dir == 2:
        to_shuffle = []
        for i in range(len(grid[0])):
            to_shuffle.append([row[i] for row in grid])
        to_shuffle = [row[::-1] for row in to_shuffle]
        turned_shuffled = shuffle_grid_left(to_shuffle)
        shuffled = []
        for i in range(len(grid) - 1, -1, -1):
            shuffled.append([row[i] for row in turned_shuffled])
    else:
        shuffled = shuffle_grid_left(deepcopy(grid))

    return shuffled

def cycle(grid):
    return shuffle(1, shuffle(2, shuffle(3, shuffle(0, grid))))

def first(grid):
    result = shuffle(0, grid)
    total = 0
    for i in range(len(result)):
        total += (i+1) * result[len(result) - 1 - i].count('O')

    return total

def second(grid):
    results = []
    current_result = deepcopy(grid)
    while current_result not in results:
        results.append(current_result)
        current_result = deepcopy(cycle(deepcopy(current_result)))

    index = results.index(current_result)
    current_iteration = len(results)
    cycle_length = current_iteration - index
    traversal_length = 1000000001 - (index - 1)
    modulo = ((traversal_length % cycle_length) - 1) % cycle_length
    result = results[index + modulo - 1]

    total = 0
    for i in range(len(result)):
        total += (i+1) * result[len(result) - 1 - i].count('O')

    return total



print(second(lines))