from itertools import permutations


UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3


class Node:
    def __init__(self, x: int, y: int, val: int):
        self.x = x
        self.y = y
        self.val = val
        self.direction = None


class PathDirector:
    def __init__(self, input_lines: list[str]):
        self.grid: list[list[Node]] = []
        for x in range(len(input_lines[0])):
            self.grid.append([])
            for y in range(len(input_lines)):
                self.grid[x].append(Node(x, y, int(input_lines[y][x])))

    def nodes(self, x, y) -> Node:
        return self.grid[x][y]

    def get_neighbors(self, x, y) -> list[Node]:
        # neighbors = permutations(range(-1, 2), 2)  # Diagonals
        neighbor_positions = [(x + x2, y + y2) for (x2, y2) in [(0, -1), (0, 1), (-1, 0), (1, 0)]
                              if 0 <= x + x2 < len(self.grid) and 0 <= y + y2 < len(self.grid[0])]
        # print(f'neighbor pos: {neighbor_positions}')
        return [self.nodes(x2, y2) for x2, y2 in neighbor_positions]

    def direct_pathing(self, target_position: (int, int), dir_sync_max: int):
        target = self.grid[target_position[0]][target_position[1]]
        # radiate to nodes surrounding, pass in sum of total value to reach the target
        # overwrite if new value is lower than that node's current value
        # (& dir_sync_max is adhered to)


