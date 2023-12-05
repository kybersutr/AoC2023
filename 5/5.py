import math
with open("input.txt", 'r') as f:
   contents = f.read()

parts = contents.split('\n\n')

seeds = [int(x) for x in parts[0].split()[1:]]

seed_to_soil = [(int(x[1]), int(x[0]), int(x[2])) for x in [y.split() for y in parts[1].split('\n')[1:]]]

soil_to_fertilizer = [(int(x[1]), int(x[0]), int(x[2])) for x in [y.split() for y in parts[2].split('\n')[1:]]]

fertilizer_to_water = [(int(x[1]), int(x[0]), int(x[2])) for x in [y.split() for y in parts[3].split('\n')[1:]]]

water_to_light = [(int(x[1]), int(x[0]), int(x[2])) for x in [y.split() for y in parts[4].split('\n')[1:]]]

light_to_temperature = [(int(x[1]), int(x[0]), int(x[2])) for x in [y.split() for y in parts[5].split('\n')[1:]]]

temperature_to_humidity = [(int(x[1]), int(x[0]), int(x[2])) for x in [y.split() for y in parts[6].split('\n')[1:]]]

humidity_to_location = [(int(x[1]), int(x[0]), int(x[2])) for x in [y.split() for y in parts[7].split('\n')[1:-1]]]

"""
interval = tuple (first_start, second_start, range)
"""

def normalise_intervals(intervals):
    normalised = []
    intervals = sorted(intervals, key=lambda x: x[0])
    current_value = 0
    for interval in intervals:
        if interval[2] == math.inf:
            continue
        if len(normalised) > 0 and interval[0] == current_value and interval[1] == normalised[-1][1] + normalised[-1][2]:
            last_interval = normalised.pop()
            normalised.append((last_interval[0], last_interval[1], last_interval[2] + interval[2]))
            current_value += interval[2]
        elif interval[0] == current_value:
            normalised.append(interval)
            current_value += interval[2]
        else:
            interval_value = interval[0]
            new_interval = (current_value, current_value, interval_value - current_value)
            normalised.append(new_interval)
            normalised.append(interval)
            current_value = interval[0] + interval[2]

    if normalised[-1][2] != math.inf:
        normalised.append((normalised[-1][0] + normalised[-1][2], normalised[-1][0] + normalised[-1][2], math.inf))

    return normalised


def find_interval_for_value(value, intervals):
    for interval in intervals:
        if value >= interval[0] and value < interval[0] + interval[2]:
            return interval

    raise ValueError(f"Could not find interval for value {value}.")


def merge_intervals(intervals1, intervals2):
    input_intervals = normalise_intervals(intervals1)
    output_intervals = normalise_intervals(intervals2)

    merged = []
    while len(input_intervals) > 0:
        interval = input_intervals[0]
        input_intervals = input_intervals[1:]
        input_value = interval[0]
        intermediate_value = interval[1]
        output_interval = find_interval_for_value(intermediate_value, output_intervals)
        output_value = output_interval[1] + (intermediate_value - output_interval[0])
        range = min(interval[2], output_interval[2] - (intermediate_value - output_interval[0]))

        merged.append((input_value, output_value, range))
        if range < interval[2]:
            input_intervals = [(input_value + range, intermediate_value + range, interval[2] - range)] + input_intervals


    return merged




seed_to_fertilizer = merge_intervals(seed_to_soil, soil_to_fertilizer)
seed_to_water = merge_intervals(seed_to_fertilizer, fertilizer_to_water)
seed_to_light = merge_intervals(seed_to_water, water_to_light)
seed_to_temperature = merge_intervals(seed_to_light, light_to_temperature)
seed_to_humidity = merge_intervals(seed_to_temperature, temperature_to_humidity)
seed_to_location = merge_intervals(seed_to_humidity, humidity_to_location)

def first():
    locations = []
    for seed in seeds:
        interval = find_interval_for_value(seed, seed_to_location)
        location = interval[1] + (seed - interval[0])
        locations.append(location)

    return(min(locations))

def second():
    min_location = math.inf
    for i in range(0, len(seeds), 2):
        seed_initial = seeds[i]
        seed_range = seeds[i+1]
        while seed_range > 0:
            interval = find_interval_for_value(seed_initial, seed_to_location)
            if interval[1] + (seed_initial - interval[0]) < min_location:
                min_location = interval[1] + (seed_initial - interval[0])

            seed_range -= interval[2] - (seed_initial - interval[0])
            seed_initial = interval[0] + interval[2]

    return(min_location)

print(second())