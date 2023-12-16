import file_ops
from timer import TimeHandler
import sys

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)
NA = (0, 0)
dirs = (UP, DOWN, LEFT, RIGHT, NA)  # access via index

class Tile:
    def __init__(self, character: str, x: int, y: int):
        # When hit a mirror, check if hit from by beam going UP, DOWN, LEFT, RIGHT
        # e.g., beam going LEFT hits the [2] for each of these (see dirs)
        self.character = character
        self.x, self.y = x, y
    def get_dir(self, direction: (int, int)):
        if self.character == '.':
            return [direction], [direction], [direction], [direction], [direction]
        if self.character == '\\':
            return [LEFT], [RIGHT], [UP], [DOWN]
        elif self.character == '|':
            return [UP], [DOWN], [UP, DOWN], [UP, DOWN]
        elif self.character == '-':
            return [LEFT, RIGHT], [LEFT, RIGHT], [LEFT], [RIGHT]
        elif self.character == '/':
            return [RIGHT], [LEFT], [DOWN], [UP]

class Beam:
    def __init__(self, dir: (int, int), x: int, y: int):
        self.dir = dir
        self.x, self.y = x, y


def get_tile_at(position: (int, int), tileset: [[]]) -> Tile:
    return tileset[position[1]][position[0]]

def beam_beams(beam: Beam):
    # Get hit tile
    next_pos = (beam.x + beam.dir[0], beam.y + beam.dir[1])
    if not 0 <= next_pos[0] <= len(tiles[0]) or not 0 <= next_pos[1] <= len(tiles):
        return  # off the grid
    beam.x, beam.y = next_pos[0], next_pos[1]
    hit_tile = get_tile_at(next_pos, tiles)
    energized_tiles.add(hit_tile)
    new_dirs = hit_tile.get_dir(beam.dir)[dirs.index(beam.dir)]
    beam.dir = new_dirs[0]
    beam_beams(beam)
    if len(new_dirs) > 1:  # create a new beam for the split
        new_beam = Beam(new_dirs[1], next_pos[0], next_pos[1])
        beam_beams(new_beam)



timer = TimeHandler()
sys.setrecursionlimit(9999999)
input_lines = file_ops.read_input(16)
tiles = []
for r, line in enumerate(input_lines):  # build the grid
    tiles.append([])
    for c, char in enumerate(line):
        tile = Tile(char, c, r)
        tiles[-1].append(tile)

# part 1
start_beam = Beam(RIGHT, -1, 0)
energized_tiles = set()
beam_beams(start_beam)
print(len(energized_tiles))


print(timer.fetch_time())
