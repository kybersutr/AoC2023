with open("input.txt", 'r') as f:
    lines = f.readlines()

def get_neighbor(position, lines, vertical_offset, horizontal_offset):
    l_index = position[0]
    ch_index = position[1]
    try:
        result = lines[l_index + horizontal_offset][ch_index + vertical_offset]
    except IndexError:
        result = '.'

    return result

def is_symbol(char):
    if not char.isnumeric() and char != '.' and char != '\n':
        print(char)
    return not char.isnumeric() and char != '.' and char != '\n'


def neighbors_symbol(position, lines):
    neighbors = [get_neighbor(position, lines, -1, -1),
                 get_neighbor(position, lines, -1, 0),
                 get_neighbor(position, lines, -1, 1),
                 get_neighbor(position, lines, 0, -1),
                 get_neighbor(position, lines, 0, 0),
                 get_neighbor(position, lines, 0, 1),
                 get_neighbor(position, lines, 1, -1),
                 get_neighbor(position, lines, 1, 0),
                 get_neighbor(position, lines, 1, 1)]

    return any([is_symbol(n) for n in neighbors])

def first(lines):
    good_numbers = []
    for l_index, line in enumerate(lines):
        current_position = 0
        num = ""
        positions = []
        while current_position < len(line):
            current_character = line[current_position]
            if current_character.isnumeric():
                num += current_character
                positions.append((l_index, current_position))
            else:
                if len(num) > 0:
                    if any(neighbors_symbol(position, lines) for position in positions):
                        good_numbers.append(num)
                num = ""
                positions = []
            current_position += 1
    return(good_numbers)

print(first(lines))
print(sum(int(number) for number in first(lines)))