
import file_ops
import re


class Range:
    def __init__(self, dest_start: str, source_start: str, length: str):
        self.dest_start = int(dest_start)
        self.source_start = int(source_start)
        self.length = int(length)

class Map:
    def __init__(self, title: str):
        self.source = title.split('-')[0]
        self.dest = title.split('-')[2].split(' ')[0]
        self.ranges: list[Range] = list()


class SeedRange:  # For part 2
    def __init__(self, str_range: str):
        self.start, self.length = int(str_range.split(' ')[0]), int(str_range.split(' ')[1])

def process_seed(analyze_seed) -> (int, int, int):
    current_type = 'seed'
    seed_number = int(analyze_seed)  # update as we convert
    max_range = math.inf  # part 2  Calculate how far away from the upper bounds of length this # is
    min_range = math.inf
    while current_type != 'location':
        # Find the correct map
        working_map = [m for m in maps if m.source == current_type][0]
        # work through each range, checking if the number is w/in bounds
        contained_in_any_range = False
        map_min_range = math.inf
        for map_range in working_map.ranges:
            if seed_number in range(map_range.source_start, map_range.source_start + map_range.length):
                # found a map containing the seed number. Do the conversion
                check_range = map_range.source_start + map_range.length - seed_number
                max_range = check_range if check_range < max_range else max_range
                # print(f'max range {max_range}')
                seed_number = seed_number - map_range.source_start + map_range.dest_start
                contained_in_any_range = True
                break
            else:  # not contained. cache the range to see which is closest in event of no match
                map_min_range = map_range.source_start - seed_number
        if not contained_in_any_range:  # cache how far under the next range it is
            min_range = map_min_range if min_range > map_min_range > 0 else min_range
        # print(f'{working_map.dest}  {seed_number}')
        current_type = working_map.dest
    return seed_number, max_range, min_range


# Parse input, build the maps
input_lines = [line for line in file_ops.read_input(5) if line != '']  # strip empty lines
int_regex = re.compile(r'\d+')
maps: list[Map] = []
for i in range(1, len(input_lines)):
    line = input_lines[i]
    if not line[0].isdecimal():  # map title. Make a new Map
        map = Map(line.split(' ')[0])
        maps.append(map)
        continue
    # Not a title. Fill the last created map's ranges
    numbers = int_regex.findall(line)
    map_range = Range(numbers[0], numbers[1], numbers[2])
    maps[-1].ranges.append(map_range)


# ____PART 1____
seeds = int_regex.findall(input_lines[0])
lowest_location = math.inf
# Work through the seed data conversions
for seed in seeds:
    location_number = process_seed(seed)[0]
    lowest_location = location_number if location_number < lowest_location else lowest_location
print(f' Part 1: {lowest_location}')


# ____PART 2____
seed_range_regex = re.compile(r'\d+ \d+')
seed_range_inputs = seed_range_regex.findall(input_lines[0])
seed_ranges = [SeedRange(sr) for sr in seed_range_inputs]
lowest_location = math.inf
print(f'total seed range count: {len(seed_ranges)}')
for i, seed_range in enumerate(seed_ranges):
    print(f'analyzing seed index {i}')
    # Process 1 seed, caching the max numbers that would pass each map in the same ranges
    # Use that to skip subsequent seeds, b/c you know they will have a higher location (prev+1)
    # Recalc the max range if a seed leaves it and has to be processed
    range_max = 0
    range_min = 0
    for seed in range(seed_range.start, seed_range.start + seed_range.length + 1):
        # print(f'max range now {range_max}')
        # print(f'min range now {range_min}')
        range_max -= 1
        range_min -= 1
        if range_max <= 0 or range_min <= 0:
            results = process_seed(seed)
            location_number = results[0]
            lowest_location = location_number if location_number < lowest_location else lowest_location
            range_max = results[1]  # if results[1] < range_max else range_max
            range_min = results[2]  # if results[2] < range_min else range_min
            print(f'seed {seed}   {location_number}  max: {range_max}   min: {range_min}')
print(f'Part 2 {lowest_location}')


