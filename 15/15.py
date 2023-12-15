with open("input.txt", 'r') as f:
    entries = [entry.strip() for entry in f.read().split(',')]

def hash(string, multiplicator, modulus):
    total = 0
    for char in string:
        total += ord(char)
        total *= multiplicator
        total = total % modulus

    return total

def first(entries):
    total = 0
    for entry in entries:
        h = hash(entry, 17, 256)
        total += h

    return(total)


def focusing_power(boxes):
    total = 0
    for i, box in enumerate(boxes):
        for j, entry in enumerate(box):
            focusing_power = (i+1)*(j+1)*entry[1]
            total += focusing_power

    return total


def second(entries):
    boxes = []
    for _ in range(256):
        boxes.append([])

    for entry in entries:
        if '-' in entry:
            label = entry.split('-')[0]
            box_id = hash(label, 17, 256)
            box = boxes[box_id]

            for i in range(len(box)):
                if box[i][0] == label:
                    box.pop(i)
                    break

        elif '=' in entry:
            label, focal_length = entry.split('=')
            focal_length = int(focal_length)
            box_id = hash(label, 17, 256)
            box = boxes[box_id]

            for i in range(len(box)):
                if box[i][0] == label:
                    box[i][1] = focal_length
                    break
            else:
                box.append([label, focal_length])
        else:
            raise ValueError(f"Invalid operation {entry}.")

    return focusing_power(boxes)

print(second(entries))