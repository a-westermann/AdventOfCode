import file_ops
from timer import TimeHandler
from path_directing import PathDirector
import sys


timer = TimeHandler()
sys.setrecursionlimit(99999)
input_lines = file_ops.read_input(23)
path_director = PathDirector(input_lines, 23)

target_node = [n for n in path_director.grid[-1] if n.val == '.'][0]
grid = path_director.direct_pathing_23(target_node)
for y in grid:
    print([n.steps_to_target for n in y])


print(timer.fetch_time())
