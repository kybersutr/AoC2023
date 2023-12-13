with open("input.txt", 'r') as f:
    grids = [[row for row in grid.split('\n') if len(row) > 0 ] for grid in f.read().split('\n\n')]

def check_mirror_row(grid, i):
    to_edge = min(i, len(grid) - i - 2)
    for j in range(to_edge + 1):
        if grid[i - j] != grid[i + 1 + j]:
            return False

    return True

def find_mirror_row(grid):
    for i in range(len(grid) - 1):
        if grid[i] == grid[i+1]:
            if check_mirror_row(grid, i):
                return i

    return -1


def find_mirror_column(grid):
    transpose = []
    for i in range(len(grid[0])):
        column = [row[i] for row in grid]
        transpose.append(column)

    return find_mirror_row(transpose)


def find_mirror(grid):
    row_mirror_index = find_mirror_row(grid)
    column_mirror_index = find_mirror_column(grid)

    return(row_mirror_index, column_mirror_index)


def first(grids):
    mirrors = [find_mirror(grid) for grid in grids]
    result = sum([(x[0] + 1) * 100 + (x[1] + 1) for x in mirrors])

    return result

def compare_strings(s1, s2):
    """
        -1 = different
        0 = same but with a smudge
        1 = same
    """
    smudge = False
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            if smudge:
                return -1
            else:
                smudge = True

    if smudge:
        return 0
    else:
        return 1

def check_mirror_row_smudge(grid, i):
    to_edge = min(i, len(grid) - i - 2)
    smudge = False
    for j in range(to_edge + 1):
        similarity =  compare_strings(grid[i - j],grid[i + 1 + j])
        if similarity == -1:
            return False
        elif similarity == 0:
            if smudge:
                return False
            else:
                smudge = True

    return smudge

def find_mirror_row_smudge(grid):
    for i in range(len(grid) - 1):
        if compare_strings(grid[i],grid[i+1]) != -1:
            if check_mirror_row_smudge(grid, i):
                return i

    return -1


def find_mirror_column_smudge(grid):
    transpose = []
    for i in range(len(grid[0])):
        column = [row[i] for row in grid]
        transpose.append(column)

    return find_mirror_row_smudge(transpose)


def find_mirror_smudge(grid):
    row_mirror_index = find_mirror_row_smudge(grid)
    column_mirror_index = find_mirror_column_smudge(grid)

    return(row_mirror_index, column_mirror_index)

def second(grids):
    mirrors = [find_mirror_smudge(grid) for grid in grids]
    print(mirrors)
    result = sum([(x[0] + 1) * 100 + (x[1] + 1) for x in mirrors])

    return result

print(first(grids))
print(second(grids))
