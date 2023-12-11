import file_ops
from timer import TimeHandler
from math import factorial


class Galaxy:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


def calc_distance(g1: Galaxy, g2: Galaxy):
    return abs(g2.x - g1.x) + abs(g2.y - g1.y)


timer = TimeHandler()
input_lines = file_ops.read_input(11)
# expand the universe
expanded_universe = []
for r, line in enumerate(input_lines):
    expanded_universe.append(line)
    if '#' not in line:
        expanded_universe.append(line)
column_count = len(input_lines[0])
added_count = 0
for c in range(column_count):
    column = [i[c] for i in input_lines]
    if '#' not in column:
        for r in range(len(expanded_universe)):
            expanded_universe[r] = (
                    expanded_universe[r][:c + added_count] + '.' + expanded_universe[r][c + added_count:])
        added_count += 1

# [print(f'row i  {l}') for l in enumerate(expanded_universe)]
# Create galaxies
galaxies = []
for r in range(len(expanded_universe)):
    for c in range(len(expanded_universe[r])):
        if expanded_universe[r][c] == '#':
            galaxy = Galaxy(c, r)
            galaxies.append(galaxy)

# calculation for # of combinations: n! / (r!(n-r)!)
# factoria(n) / (factorial(r) * factrorial(n-r))
# path does not include diagonals - therefor  d=abs(x2-x1)+abs(y2-y1)
sum_length = 0
for i, galaxy in enumerate(galaxies):
    for galaxy2 in galaxies[i + 1:]:
        distance = calc_distance(galaxy, galaxy2)
        sum_length += distance
        # print(f'{galaxy.x}/{galaxy.y} distance from {galaxy2.x}/{galaxy2.y}  =  {distance}')



print(f'Part 1: {sum_length}')  # 0.03 seconds
print(timer.fetch_time())
