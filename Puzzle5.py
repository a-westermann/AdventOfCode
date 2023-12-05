import math

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


class SeedRange:
    def __init__(self, str_range: str):
        self.start, self.end = str_range.split(' ')[0], str_range.split(' ')[1]


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
seed_range_regex = re.compile(r'\d+ \d+')

lowest_location = math.inf
# Work through the seed data conversions
for seed in seeds:
    current_type = 'seed'
    seed_number = int(seed)  # update as we convert
    while current_type != 'location':
        # Find the correct map
        working_map = [m for m in maps if m.source == current_type][0]
        # work through each range, checking if the number is w/in bounds
        number_contained = False
        for map_range in working_map.ranges:
            if seed_number in range(map_range.source_start, map_range.source_start + map_range.length):
                # found a map containing the seed number. Do the conversion
                seed_number = seed_number - map_range.source_start + map_range.dest_start
                number_contained = True
                break
            # If no map range was found, just leave the number alone
        current_type = working_map.dest
    lowest_location = seed_number if seed_number < lowest_location else lowest_location
print(lowest_location)

# ____PART 2____
seed_range_inputs = seed_range_regex.findall(input_lines[0])
seed_ranges = [SeedRange(sr) for sr in seed_range_inputs]


