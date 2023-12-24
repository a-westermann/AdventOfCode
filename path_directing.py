import math
from itertools import permutations


UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3
def get_oppisite_dir_23(direction):
    # Could have made these (int, int) instead, but would have to refactor get_neighbors
    if direction == UP: return DOWN
    if direction == DOWN: return UP
    if direction == LEFT: return RIGHT
    if direction == RIGHT: return LEFT
    return None

class Node:
    def __init__(self, x: int, y: int, val: str, puzzle: int):
        self.x = x
        self.y = y
        self.val = val
        self.steps_to_target = 9999
        self.direction = -1
        if puzzle == 23:
            self.slope = None
            self.steps_to_target = 0
            self.steps_to_target = dict()
            if val == '^': self.slope = UP
            elif val == 'v': self.slope = DOWN
            elif val == '>': self.slope = RIGHT
            elif val == '<': self.slope = LEFT
            self.children = dict()  # all children nodes tupel
            self.prev_dir = -1
        self.parent_node = dict()  # the node that this one leads to. Avoid backtracking
        # specific to 17 :
        self.val_to_target = math.inf
        self.straight_count = 1

    def set_steps(self, steps):
        self.steps_to_target = 0

    # def delete_children_recursively(self):
    #     # found a longer path, clear out all children paths
    #     [c.set_steps(0) for c in self.children[::-1]]
    #     [c.children.clear() for c in self.children[::-1]]
    #     self.children.clear()
    #
    # def redo_steps_recrusively(self, steps):
    #     self.steps_to_target = steps
    #     for i, c in enumerate(self.children):
    #         c.steps_to_target = self.steps_to_target + 1 + i


class PathDirector:
    def __init__(self, input_lines: list[str], puzzle: int):
        self.grid: list[list[Node]] = []
        self.queue = []
        for y in range(len(input_lines)):
            self.grid.append([])
            for x in range(len(input_lines[0])):
                self.grid[y].append(Node(x, y, input_lines[y][x], puzzle))

    def nodes(self, y, x) -> Node:
        return self.grid[y][x]

    def get_neighbors(self, yx) -> list[tuple[Node, int]]:  # the int in the tuple is direction
        # neighbors = permutations(range(-1, 2), 2)  # Diagonals
        neighbor_positions = [((yx[1] + x2, yx[0] + y2), i) for i, (x2, y2) in
                              enumerate([(0, -1), (0, 1), (-1, 0), (1, 0)])
                              # enumerate([(0, -1), (0, 1), (-1, 0), (1, 0)])
                              if 0 <= yx[1] + x2 < len(self.grid[0]) and 0 <= yx[0] + y2 < len(self.grid)]
        # print(f'neighbor pos: {neighbor_positions}')
        return [(self.nodes(y2, x2), i) for (x2, y2), i in neighbor_positions]


# 23
    def direct_pathing_23(self, target: Node):
        # paths = enumerate(target.steps_to_target.copy())
        paths = dict()
        neighbors = self.get_neighbors((target.y, target.x))
        for e in target.steps_to_target.keys():
            paths[e] = target.steps_to_target[e]
        for path_index in paths.keys():
            steps = paths[path_index]
            for index in range(len(neighbors)):
                n = neighbors[index][0]
                i = neighbors[index][1]
                # if n == target.parent_node or n.val == '#':
                if n.val == '#' \
                    or (path_index in target.children.keys()
                    and n in target.children[path_index]) \
                    or (path_index in target.parent_node.keys()
                        and n == target.parent_node[path_index]):
                        # or target in n.children:  # PART 2
                        # or (n.val != '.' and i != get_oppisite_dir_23(n.slope)):  # PART 1
                    continue  # no backtracking, skip rocks
                target.steps_to_target[path_index + index] = steps
                n.steps_to_target[path_index + index] = steps + 1
                # if target.steps_to_target + 1 > n.steps_to_target:
                # found farther path. Update neighbor & add to queue
                self.queue.append(n)
                # n.steps_to_target = target.steps_to_target + 1
                # n.direction = i
                # n.parent_node = target
                n.parent_node[path_index + index] = target
                # sort queue so prioritize the high step nodes, to avoid path duplication
                # self.queue.sort(key=lambda x: x.steps_to_target, reverse=True)
                # if path_index + index >= len(target.children):
                #     target.children.append([])
                if path_index + index not in target.children.keys():
                    target.children[path_index + index] = []
                target.children[path_index + index].append(n)
        if len(self.queue) == 0:
            return self.grid
        next_node = self.queue.pop(0)
        return self.direct_pathing_23(next_node)


# 21
    def get_neighbors_21_pt2(self, yx) -> list[tuple[Node, int]]:  # the int in the tuple is direction
        neighbor_positions = [((yx[1] + x2, yx[0] + y2), i) for i, (x2, y2) in
                              enumerate([(0, -1), (0, 1), (-1, 0), (1, 0)])
                              # enumerate([(0, -1), (0, 1), (-1, 0), (1, 0)])
                              ]
        # print(f'neighbor pos: {neighbor_positions}')
        return [(self.nodes(y2, x2), i) for (x2, y2), i in neighbor_positions]


    def direct_pathing_21(self, target_position: (int, int)):
        target = self.nodes(target_position[0], target_position[1])
        for n, i in self.get_neighbors(target_position):
            if n == target.parent_node or n.val == '#':
                continue  # no backtracking
            if target.steps_to_target + 1 < n.steps_to_target:
                # found closer node. update steps
                n.steps_to_target = target.steps_to_target + 1
                n.direction = i
                n.parent_node = target
                # if n not in self.queue:
                self.queue.append(n)
        if len(self.queue) == 0:
            return self.grid
        next_node = self.queue.pop(0)
        return self.direct_pathing_21((next_node.y, next_node.x))



# 17
    def direct_pathing_17(self, target_position: (int, int), dir_sync_max: int):
        target = self.grid[target_position[0]][target_position[1]]
        if target.direction == -1:
            target.val_to_target = int(target.val)  # final target
            target.straight_count = 1
        # radiate to nodes surrounding, pass in sum of total value to reach the target
        # overwrite if new value is lower than that node's current value
        # (& dir_sync_max is adhered to)
        for n, i in self.get_neighbors(target_position):
            if n == target.parent_node or \
                    (i == target.direction and  # -1 to handle the final target
                    target.straight_count == dir_sync_max):
                continue  # hit the max straight concurrent directions
            if target.val_to_target + int(n.val) < n.val_to_target:
                # found a lower value target. Update the path for this node & propogate
                n.val_to_target = int(n.val) + target.val_to_target
                n.direction = i
                n.parent_node = target
                if i == target.direction or target.direction == -1:  # update the straight count
                    n.straight_count = target.straight_count + 1
                # if n not in self.queue:
                self.queue.append(n)
        if len(self.queue) == 0:
            return self.grid
        next_node = self.queue.pop(0)
        return self.direct_pathing_17((next_node.x, next_node.y), dir_sync_max)
