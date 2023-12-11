with open("input.txt", 'r') as f:
    lines = f.readlines()

sequences = [list(map(lambda x: int(x), line.split())) for line in lines]

def get_next(sequence):
    if all(x == 0 for x in sequence):
        return 0

    differences = [sequence[i+1] - sequence[i] for i in range(len(sequence) - 1)]

    return sequence[-1] + get_next(differences)

def first(seq):
    total = 0
    for sequence in seq:
        total += get_next(sequence)

    return total

def second(seq):
    return first([list(reversed(x)) for x in seq])

print(first(sequences))
print(second(sequences))