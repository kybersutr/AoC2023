import math

with open("input.txt", 'r') as f:
    lines = [line.strip() for line in f.readlines()]

letter_to_dir = \
    {
        '|' : {'u', 'd'},
        '-' : {'l', 'r'},
        'L' : {'u', 'r'},
        'J' : {'u', 'l'},
        '7' : {'d', 'l'},
        'F' : {'d', 'r'},
        '.' : set(),
        'S' : {'l', 'r'}
    }


def get_s_index(lines):
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == 'S':
                s_index = (i, j)
                return s_index


s_index = get_s_index(lines)
print(s_index)


pipes = [[letter_to_dir[letter] for letter in row] for row in lines]

def first(pipes, s_index):
    to_go = [(s_index, 0, [])]

    opposite = \
        {
            'u': 'd',
            'l': 'r',
            'd': 'u',
            'r': 'l'
        }

    dir_to_pos = \
        {
            'u': lambda x: (x[0] - 1, x[1]),
            'l': lambda x: (x[0], x[1] - 1),
            'd': lambda x: (x[0] + 1, x[1]),
            'r': lambda x: (x[0], x[1] + 1)
        }

    while len(to_go) != 0:
        current = to_go.pop(0)
        position = current[0]
        steps = current[1]
        path = current[2]
        pipe = pipes[position[0]][position[1]]

        for dir in pipe:
            new_position = dir_to_pos[dir](position)
            if len(path) > 0 and new_position == path[-1]:
                continue
            if new_position == s_index:
                return math.ceil(steps/2)

            try:
                neighbor = pipes[new_position[0]][new_position[1]]
            except:
                continue

            if opposite[dir] in neighbor:
                to_go.append((new_position, steps+1, path + [position]))

    return -1

def get_path(pipes, s_index):
    to_go = [(s_index, 0, [])]

    opposite = \
        {
            'u': 'd',
            'l': 'r',
            'd': 'u',
            'r': 'l'
        }

    dir_to_pos = \
        {
            'u': lambda x: (x[0] - 1, x[1]),
            'l': lambda x: (x[0], x[1] - 1),
            'd': lambda x: (x[0] + 1, x[1]),
            'r': lambda x: (x[0], x[1] + 1)
        }

    while len(to_go) != 0:
        current = to_go.pop(0)
        position = current[0]
        steps = current[1]
        path = current[2]
        pipe = pipes[position[0]][position[1]]

        for dir in pipe:
            new_position = dir_to_pos[dir](position)
            if len(path) > 0 and new_position == path[-1]:
                continue
            if new_position == s_index:
                path.append(position)
                return path

            try:
                neighbor = pipes[new_position[0]][new_position[1]]
            except:
                continue

            if opposite[dir] in neighbor:
                to_go.append((new_position, steps + 1, path + [position]))

    return -1

def sort_by_lines(path):
    rows = [[] for i in range(len(lines))]
    for position in path:
        rows[position[0]].append(position)

    rows = [sorted(row) for row in rows]
    return rows


def get_segments(pipeline, indices, length):
    count = 0
    up = False
    down = False
    print(indices)
    print(pipeline)

    for i in range(length):
        if i in indices:
            if 'u' in pipeline[i]:
                up = not up
            if 'd' in pipeline[i]:
                down = not down
        elif up or down:
            count += 1

    print(count)
    return(count)



def second(path_rows, pipes):
    total = 0
    for r_index, row in enumerate(path_rows):
        indices = [x[1] for x in row]
        length = len(pipes[r_index])
        total += get_segments(pipes[r_index], indices, length)

    return total


path = get_path(pipes, s_index)
print(len(path))
by_rows = sort_by_lines(path)
print(second(by_rows, pipes))



