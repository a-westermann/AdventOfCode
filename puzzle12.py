import file_ops
from timer import TimeHandler
import re
from functools import cache


queue = set()  # set to avoid duplication
@cache
def process_layout(full_layout: str, index: int):
    # next_q = re.search(r'?', full_layout[index:])
    next_q = full_layout[index:].find('?')
    if next_q != -1:
        next_i = next_q + index
        for x in ('.', '#'):
            permutation = full_layout[:next_i] + x + full_layout[next_i + 1:]
            # print(permutation)
            queue.add((permutation, next_i))
            permutations.add((permutation, next_i))




timer = TimeHandler()
input_lines = file_ops.read_input(12)

# Work from outside in?
for line in input_lines:
    layout, instructions = line.split(' ')
    conditions = [n for n in instructions.split(',')]
    permutations = set()
    queue.add((layout, 0))
    while len(queue) > 0:
        springs, index_start = queue.pop()
        process_layout(springs, index_start)
    # break



print(timer.fetch_time())
