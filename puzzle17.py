import file_ops
from timer import TimeHandler
from path_directing import PathDirector, Node


timer = TimeHandler()
input_lines = file_ops.read_input(17)
path_director = PathDirector(input_lines)
for r in path_director.grid:
    print(''.join(str(node.val) for node in r))

# part 1
r = path_director.direct_pathing((len(path_director.grid) - 1, len(path_director.grid[0]) - 1), 3)

print(timer.fetch_time())
