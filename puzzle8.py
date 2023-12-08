import file_ops
from timer import TimeHandler
import re


class Node:
    def __init__(self, origin: str, destination: (str, str)):
        self.origin = origin
        self.destination = destination


timer = TimeHandler()
input_lines = file_ops.read_input(8)

# create a dictionary of the nodes
nodes = {}
for line in input_lines[2:]:
    points = re.findall(r'\w+|[^\w \t=(,)]', line)
    node = Node(points[0], (points[1], points[2]))
    nodes[node.origin] = node.destination

# get the directions & convert to 0/1 index
directions = input_lines[0].replace('L', '0').replace('R', '1')
step_count = 0

current_point = 'AAA'
while current_point != 'ZZZ':
    current_point = nodes[current_point][int(directions[step_count % len(directions)])]
    # print(current_point)
    step_count += 1


print(f'Part 1 Steps: {step_count}')
print(timer.fetch_time())
