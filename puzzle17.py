import file_ops
from timer import TimeHandler
from path_directing import PathDirector, Node
import sys


timer = TimeHandler()
input_lines = file_ops.read_input(17)
path_director = PathDirector(input_lines)
for r in path_director.grid:
    print(''.join(str(node.val) for node in r))

# part 1
sys.setrecursionlimit(999999)
# val_grid = path_director.direct_pathing((len(path_director.grid[0]) - 1, len(path_director.grid) - 1), 3)
val_grid = path_director.direct_pathing((0, 0), 3)
for row in val_grid:
    print([r.val_to_target for r in row])
for row in val_grid:
    print([r.direction for r in row])
print(f'Part 1: {path_director.nodes(len(path_director.grid[0]) - 1, len(path_director.grid) - 1).val_to_target}')
print(timer.fetch_time())
