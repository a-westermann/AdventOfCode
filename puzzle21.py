import file_ops
from timer import TimeHandler
from path_directing import PathDirector
import sys


timer = TimeHandler()
sys.setrecursionlimit(99999)
input_lines = file_ops.read_input(21)

path_director = PathDirector(input_lines)

start_node = None
# start_node = [n for n in y for y in path_director.grid if n.val == 'S'][0]
for y in path_director.grid:
    # print([n.val for n in y])
    for node in y:
        if node.val == 'S':
            start_node = node

start_node.steps_to_target = 0
path_director.grid = path_director.direct_pathing_21((start_node.y, start_node.x))
# for y in path_director.grid:
#     print([n.steps_to_target for n in y])

total_reachable = 0
pt2_reachable = 0
# pt2_multiplier = 26501365 / len(path_director.grid[0])
# grid_multi = int(26501365 / 130)
# leftover = 26501365 % 130
# print(f'{grid_multi}   {leftover}')
for y in path_director.grid:
    for n in y:
        total_reachable += 1 if n.steps_to_target <= 64 and n.steps_to_target % 2 == 0 else 0
        # pt2_reachable += 1 if n.steps_to_target % 2 != 0 else 0
print(f'Part 1: {total_reachable}')  # 0.09 seconds
# print(f'Part 2: {pt2_reachable * grid_multi + int(.653 * pt2_reachable)}')
print(timer.fetch_time())
