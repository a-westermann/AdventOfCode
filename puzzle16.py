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
        self.character = character
        self.x, self.y = x, y
        self.beam_history = set()

    def get_dir(self, direction: (int, int)):
        if direction in self.beam_history:
            return None  # already had a beam pass this way. No need to repeat
        self.beam_history.add(direction)
        # When hit a mirror, check if hit by beam going UP, DOWN, LEFT, RIGHT
        # e.g., beam going LEFT hits the [2] for each of these (see dirs above)
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
    if not 0 <= next_pos[0] < len(tiles[0]) or not 0 <= next_pos[1] < len(tiles):
        return  # off the grid
    beam.x, beam.y = next_pos[0], next_pos[1]
    hit_tile = get_tile_at(next_pos, tiles)
    energized_tiles.add(hit_tile)
    tile_dirs = hit_tile.get_dir(beam.dir)
    if not tile_dirs:
        return  # already sent a beam this way on this tile. No need to repeat
    new_dirs = tile_dirs[dirs.index(beam.dir)]
    beam.dir = new_dirs[0]
    beam_beams(beam)
    if len(new_dirs) > 1:  # create a new beam for the split
        new_beam = Beam(new_dirs[1], next_pos[0], next_pos[1])
        beam_beams(new_beam)


timer = TimeHandler()
sys.setrecursionlimit(9999)
input_lines = file_ops.read_input(16)
tiles = []
for r, line in enumerate(input_lines):  # build the grid
    tiles.append([])
    for c, char in enumerate(line):
        tile = Tile(char, c, r)
        tiles[-1].append(tile)

start_beam = Beam(RIGHT, -1, 0)
energized_tiles = set()
beam_beams(start_beam)
print(f'Part 1 : {len(energized_tiles)}')  # 0.05 seconds
p2_energized_count = len(energized_tiles)
start_beam.x, start_beam.y = -1, 0
start_beam.dir = RIGHT
beam_x, beam_y = -1, 0
beam_dir = RIGHT
while start_beam.y < len(tiles):
    energized_tiles.clear()
    [[t.beam_history.clear() for t in _] for _ in tiles]
    beam_beams(start_beam)
    p2_energized_count = p2_energized_count if \
        p2_energized_count > len(energized_tiles) else len(energized_tiles)
    beam_y += 1
    start_beam = Beam(beam_dir, beam_x, beam_y)
    if start_beam.y == len(tiles):  # flip to right or break
        if start_beam.x == len(tiles[0]):
            break  # finished right side
        beam_x = len(tiles[0])
        beam_y = 0
        beam_dir = LEFT
        start_beam.x = len(tiles[0])  # start 1 space outside len
        start_beam.y = 0
        start_beam.dir = LEFT
# Now hit the top / bottom rows
start_beam.x, start_beam.y = 0, -1
beam_x, beam_y = 0, -1
start_beam.dir = DOWN
beam_dir = DOWN
while start_beam.x < len(tiles[0]):
    energized_tiles.clear()
    [[t.beam_history.clear() for t in _] for _ in tiles]
    beam_beams(start_beam)
    p2_energized_count = p2_energized_count if \
        p2_energized_count > len(energized_tiles) else len(energized_tiles)
    beam_x += 1
    start_beam = Beam(beam_dir, beam_x, beam_y)
    if start_beam.x == len(tiles[0]):  # flip to bottom or break
        if start_beam.y == len(tiles):
            break  # finished bottom
        beam_x = 0
        beam_y = len(tiles)
        beam_dir = UP
        start_beam.y = len(tiles)
        start_beam.x = 0
        start_beam.dir = UP

print(f'Part 2 {p2_energized_count}')  # 8.35 seconds
print(timer.fetch_time())
