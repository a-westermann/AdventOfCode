import math
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
        self.val_to_target = math.inf
        self.direction = -1
        self.straight_count = 1
        self.parent_node = None  # the node that this one leads to. Avoid backtracking


class PathDirector:
    def __init__(self, input_lines: list[str]):
        self.grid: list[list[Node]] = []
        self.queue = []
        for x in range(len(input_lines[0])):
            self.grid.append([])
            for y in range(len(input_lines)):
                self.grid[x].append(Node(x, y, int(input_lines[y][x])))

    def nodes(self, x, y) -> Node:
        return self.grid[x][y]

    def get_neighbors(self, xy) -> list[tuple[Node, int]]:
        # neighbors = permutations(range(-1, 2), 2)  # Diagonals
        neighbor_positions = [((xy[0] + x2, xy[1] + y2), i) for i, (x2, y2) in
                              enumerate([(-1, 0), (1, 0), (0, -1), (0, 1)])
                              # enumerate([(0, -1), (0, 1), (-1, 0), (1, 0)])
                              if 0 <= xy[0] + x2 < len(self.grid) and 0 <= xy[1] + y2 < len(self.grid[0])]
        # print(f'neighbor pos: {neighbor_positions}')
        return [(self.nodes(x2, y2), i) for (x2, y2), i in neighbor_positions]

    def direct_pathing(self, target_position: (int, int), dir_sync_max: int):
        target = self.grid[target_position[0]][target_position[1]]
        if target.direction == -1:
            target.val_to_target = target.val  # final target
            target.straight_count = 1
        # radiate to nodes surrounding, pass in sum of total value to reach the target
        # overwrite if new value is lower than that node's current value
        # (& dir_sync_max is adhered to)
        for n, i in self.get_neighbors(target_position):
            if n == target.parent_node or \
                    (i == target.direction and  # -1 to handle the final target
                    target.straight_count == dir_sync_max):
                continue  # hit the max straight concurrent directions
            if target.val_to_target + n.val < n.val_to_target:
                # found a lower value target. Update the path for this node & propogate
                n.val_to_target = n.val + target.val_to_target
                n.direction = i
                n.parent_node = target
                if i == target.direction or target.direction == -1:  # update the straight count
                    n.straight_count = target.straight_count + 1
                # if n not in self.queue:
                self.queue.append(n)
        if len(self.queue) == 0:
            return self.grid
        next_node = self.queue.pop(0)
        return self.direct_pathing((next_node.x, next_node.y), dir_sync_max)
