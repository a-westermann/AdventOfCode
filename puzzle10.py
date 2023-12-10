import file_ops
from timer import TimeHandler
import sys


UP = (0, 1)
DOWN = (0, -1)
LEFT = (-1, 0)
RIGHT = (1, 0)

class Pipe:
    def __init__(self, position: (int, int), tile: str):
        self.position = position
        self.tile = tile
        self.main_loop = False
        self.connnections = []
        if tile == '|': self.connnections.extend([UP, DOWN])
        elif tile == '-': self.connnections.extend([LEFT, RIGHT])
        elif tile == 'L': self.connnections.extend([UP, RIGHT])
        elif tile == 'J': self.connnections.extend([UP, LEFT])
        elif tile == '7': self.connnections.extend([DOWN, LEFT])
        elif tile == 'F': self.connnections.extend([DOWN, RIGHT])
        elif tile == '.': pass  # ground, no pipe
        elif tile == 'S': self.connnections.extend([UP, DOWN, LEFT, RIGHT])  # start. possibly has all connections

def check_connections_valid(origin: Pipe, end: Pipe) -> bool:
    direction = (end.position[0] - origin.position[0], end.position[1] - origin.position[1])
    # ^ e.g., end pipe is DOWN from origin pipe
    # check if -DOWN (UP) is a valid connection for the end pipe
    return (-direction[0], -direction[1]) in end.connnections

def traverse_pipe(origin: Pipe, last_dir: (int, int), steps: int) -> int:
    next_dir = origin.connnections[0] if last_dir != origin.connnections[0] else origin.connnections[1]
    joined_pipe = points[(origin.position[0] + next_dir[0], origin.position[1] + next_dir[1])]
    steps += 1
    joined_pipe.main_loop = True
    # print(f'steps:  {steps}      tile: {joined_pipe.tile}')
    if joined_pipe.tile == 'S':
        return steps
    else:
        return traverse_pipe(joined_pipe, (-next_dir[0], -next_dir[1]), steps)


timer = TimeHandler()
sys.setrecursionlimit(999999)
input_lines = file_ops.read_input(10)
points = dict()  # dict Key:Position Value:Pipe
start = None
# Read it in bottom to top to match up/down visually
for y, line in enumerate(input_lines[::-1]):
    for x, char in enumerate(line):
        pipe = Pipe((x, y), char)
        points[(x, y)] = pipe
        if char == 'S':
            start = pipe
            start.main_loop = True

print(f'start position:  {start.position}')
p1_farthest_steps = 0
p2_enclosed_tiles = 0
for connection in start.connnections:
    next_pipe = points[(start.position[0] + connection[0], start.position[1] + connection[1])]
    next_pipe.main_loop = True
    # print(f'{next_pipe.position}  {next_pipe.tile}  {next_pipe.connnections}')
    if check_connections_valid(start, next_pipe):
        p1_farthest_steps = traverse_pipe(next_pipe, (-connection[0], -connection[1]), 1) / 2
        # Should only have to go 1 way and then divide by 2
        # alternatively, could go both ways simultaneously and quit when reach same position
        break

# Visualization
visual_loop = []
for y, line in enumerate(input_lines[::-1]):
    loop = [x for x, c in enumerate(line) if points[x, y].main_loop]
    loop_line = ''
    for x, c in enumerate(line):
        loop_line += c if x in loop else '+'
    visual_loop.append(loop_line)
visual_loop.reverse()
for line in visual_loop:
    print(line)


print(f'Part 1: {p1_farthest_steps}')  # 0.09 seconds
print(f'Part 2: {p2_enclosed_tiles}')  #
print(timer.fetch_time())
