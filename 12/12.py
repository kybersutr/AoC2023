import itertools

with open("mini_input.txt", 'r') as f:
    lines = [l.strip() for l in f.readlines() if len(l) > 0]

springs = [(spring[0], [int(num) for num in spring[1].split(',')]) for spring in [line.split() for line in lines]]

def is_valid(string, counts):
    parts = [part for part in string.split('.') if len(part) > 0]

    return [len(x) for x in parts] == counts

def satisfy_spring(string, counts):
    possibilities = set()
    present_count = string.count('#')
    to_place = sum(counts) - present_count
    empty_indices = [i for i, char in enumerate(string) if char == '?']
    print(len(list(itertools.combinations(empty_indices, to_place))))
    for combination in itertools.combinations(empty_indices, to_place):
        new_string = ''
        for i, ch in enumerate(string):
            if ch != '?':
                new_string += ch
            elif i in combination:
                new_string += '#'
            else:
                new_string += '.'

        if is_valid(new_string, counts):
            possibilities.add(new_string)

    return possibilities

def first(springs):
    count = 0
    for i, spring in enumerate(springs):
        print(f"{i}/{len(springs)}")
        possibilities = satisfy_spring(spring[0], spring[1])
        count += len(possibilities)

    return count

def get_placements(string, counts):
    pass

def recursively_place_spring(string, counts, current_index):
    present_count = string.count('#')
    to_place = sum(counts[current_index:]) - present_count
    empty_indices = [i for i, char in enumerate(string) if char == '?']
    possible_to_place = (present_count + len(empty_indices) >= to_place) and len(string) >= sum(counts[current_index:]) + len(counts[current_index:]) - 1
    if current_index >= len(counts):
        return (True, {''})
    elif not possible_to_place:
        return (False, set())
    else:
        placement_indices = get_placements(string, counts[current_index])
        if len(placement_indices) == 0:
            return (False, set())
        for placement_index in placement_indices:
            subpossibilites = recursively_place_spring(string[placement_index + counts[current_index]], )


def satisfy_spring_smarter(string, counts):
    """
    vezmi string a první index,
    namapuj index a odtrhni začátek stringu, pošli zbytek rekurentně dál
    """

    return recursively_place_spring(string, counts, 0)

def second(springs):
    unfolded_springs = []
    for spring in springs:
        new_spring = f"{spring[0]}?{spring[0]}?{spring[0]}?{spring[0]}?{spring[0]}"
        new_counts = 5 * spring[1]
        unfolded_springs.append((new_spring, new_counts))

    count = 0
    for i, spring in enumerate(unfolded_springs):
        print(f"{i+1}/{len(springs)}")
        possibilities = satisfy_spring_smarter(spring[0], spring[1])
        count += len(possibilities)

    return count


print(second(springs))
