import file_ops
from timer import TimeHandler


class Galaxy:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


def expand(input_lines):
    expanded = []
    empty_columns, empty_rows = [], []
    for r, line in enumerate(input_lines):
        expanded.append(line)
        if '#' not in line:
            empty_rows.append(r)
    column_count = len(input_lines[0])
    for c in range(column_count):
        column = [i[c] for i in input_lines]
        if '#' not in column:
            empty_columns.append(c)
    return empty_rows, empty_columns

def calc_distance(g1: Galaxy, g2: Galaxy, exp_factor: int, empty_rows, empty_columns):
    exp_factor -= 1
    g1_new_x = g1.x + len([c for c in empty_columns if c < g1.x]) * exp_factor
    g1_new_y = g1.y + len([r for r in empty_rows if r < g1.y]) * exp_factor
    g2_new_x = g2.x + len([c for c in empty_columns if c < g2.x]) * exp_factor
    g2_new_y = g2.y + len([r for r in empty_rows if r < g2.y]) * exp_factor
    return abs(g2_new_x - g1_new_x) + abs(g2_new_y - g1_new_y)


timer = TimeHandler()
input_lines = file_ops.read_input(11)

expansion_factor = 1000000  # part 1 = 2,  part 2 = 1000000
# Brute force by actually adding rows/columns would take ~16 hours for part 2
empty_row_indices, empty_column_indices = expand(input_lines)

# Create galaxies
galaxies = []
for r in range(len(input_lines)):
    for c in range(len(input_lines[r])):
        if input_lines[r][c] == '#':
            galaxy = Galaxy(c, r)
            galaxies.append(galaxy)

# path does not include diagonals - therefor  d=abs(x2-x1)+abs(y2-y1)
sum_length = 0
for i, galaxy in enumerate(galaxies):
    for galaxy2 in galaxies[i + 1:]:
        distance = calc_distance(galaxy, galaxy2, expansion_factor, empty_row_indices, empty_column_indices)
        sum_length += distance

print(f'{sum_length}')  # Part 2 = 0.25 seconds
print(timer.fetch_time())
