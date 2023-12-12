import file_ops
from timer import TimeHandler


timer = TimeHandler()
input_lines = file_ops.read_input(12)

# Work from outside in?
for line in input_lines:
    layout, instructions = line.split(' ')
    conditions = [n for n in instructions.split(',')]
    possible_layouts = []
    for spring in layout:
        current_spring = spring
        while current_spring == '#':




print(timer.fetch_time())
