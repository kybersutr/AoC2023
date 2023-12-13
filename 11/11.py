import math

with open("input.txt", 'r') as f:
    lines = [line.strip() for line in f.readlines() if len(line) > 0]

exp_rows = set()
exp_cols = set()

for r_index, row in enumerate(lines):
    if all([x == '.' for x in row]):
        exp_rows.add(r_index)

for c_index in range(len(lines[0])):
    if all([x == '.' for x in [row[c_index] for row in lines]]):
        exp_cols.add(c_index)

galaxies = set()
for r_index in range(len(lines)):
    for c_index in range(len(lines[r_index])):
        if lines[r_index][c_index] == '#':
            galaxies.add((r_index, c_index))

def first(galaxies, exp_rows, exp_cols):
    total = 0
    for galaxy1 in galaxies:
        for galaxy2 in galaxies:
            distance = abs(galaxy2[0] - galaxy1[0]) + abs(galaxy2[1] - galaxy1[1])

            for r_index in range(min(galaxy1[0], galaxy2[0]), max(galaxy1[0], galaxy2[0])):
                if r_index in exp_rows:
                    distance += 1

            for c_index in range(min(galaxy1[1], galaxy2[1]), max(galaxy1[1], galaxy2[1])):
                if c_index in exp_cols:
                    distance += 1

            total += distance

    return total / 2

def second(galaxies, exp_rows, exp_cols):
    total = 0
    for galaxy1 in galaxies:
        for galaxy2 in galaxies:
            distance = abs(galaxy2[0] - galaxy1[0]) + abs(galaxy2[1] - galaxy1[1])

            for r_index in range(min(galaxy1[0], galaxy2[0]), max(galaxy1[0], galaxy2[0])):
                if r_index in exp_rows:
                    distance += 1000000 - 1

            for c_index in range(min(galaxy1[1], galaxy2[1]), max(galaxy1[1], galaxy2[1])):
                if c_index in exp_cols:
                    distance += 1000000 - 1

            total += distance

    return total / 2


print(first(galaxies, exp_rows, exp_cols))
print(second(galaxies, exp_rows, exp_cols))