import file_ops
import re


class Range:
    def __init__(self, dest_start: int, source_start: int, length: int):
        self.dest_start = dest_start
        self.source_start = source_start
        self.length = length

class Map:
    def __init__(self, title: str):
        self.title = title
        self.ranges: list[Range] = list()


input_lines = [line for line in file_ops.read_input(5) if line != '']  # strip empty lines
int_regex = re.compile(r'\d+')
seeds = int_regex.findall(input_lines[0])
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
