import math
import sys
import file_ops
from timer import TimeHandler
import re


def traverse_node(origin: str, instance_steps: int, pt2: bool = False):
    destination = nodes[origin][int(directions[instance_steps % len(directions)])]
    if not pt2 and destination == 'ZZZ':  # Part 1
        return instance_steps + 1
    if pt2 and destination[2] == 'Z':  # Part 2
        return instance_steps + 1
    return traverse_node(destination, instance_steps + 1, pt2)


timer = TimeHandler()
input_lines = file_ops.read_input(8)
# create a dictionary of the nodes
nodes = {}
for line in input_lines[2:]:
    points = re.findall(r'\w+|[^\w \t=(,)]', line)
    nodes[points[0]] = (points[1], points[2])


# get the directions & convert to 0/1 index
directions = input_lines[0].replace('L', '0').replace('R', '1')
step_count = 0
sys.setrecursionlimit(99999)

current_point = 'AAA'  # Part 1
step_count = traverse_node(current_point, step_count)
print(f'Part 1 Steps: {step_count}')   # 0.01 seconds

current_points = [n for n in nodes if n[2] == 'A']  # Part 2
step_counts = [traverse_node(origin, 0, True) for origin in current_points]

lowest_common_multiple = 1
for steps in step_counts:
    lowest_common_multiple = math.lcm(lowest_common_multiple, steps)
print(f'Part 2 Steps: {lowest_common_multiple}')  # 0.05 seconds
print(timer.fetch_time())
