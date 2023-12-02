import file_ops


class CubePull:
    def __init__(self):
        self.colors = {'red':0, 'green':0, 'blue':0}

class Game:
    def __init__(self, game_id: int):
        self.game_id = game_id
        self.pulls:list[CubePull] = []
        self.possible = True


def parse_pull(pull_input: str) -> CubePull:
    # separate out the colors & fill the class object
    colors = pull_input.split(',')
    cube_pull_results = CubePull()
    for color in colors:
        color_name = color.split(' ')[2]
        cube_pull_results.colors[color_name] = int(color.split(' ')[1])
    # print(f'{cube_pull_results.red} {cube_pull_results.green} {cube_pull_results.blue}')
    return cube_pull_results


maxes = {'red':12, 'green':13, 'blue':14}
possible_game_sum = 0
cube_powers_sum = 0

input_lines = file_ops.read_input(2)
for line in input_lines:
    game = Game(int(line.split(' ')[1].split(':')[0]))
    # iterate through pulls in the game and fill object
    pulls = line.strip('\n').split(':')[1].split(';')
    for pull_str in pulls:
        result_pull = parse_pull(pull_str)
        game.pulls.append(result_pull)
        # part 1
        if result_pull.colors['red'] > maxes['red'] or result_pull.colors['green'] > maxes['green'] \
          or result_pull.colors['blue'] > maxes['blue']:
            game.possible = False
    possible_game_sum += game.game_id if game.possible else 0
    # part 2  Get the maxes for each game
    max_red, max_green, max_blue = 0,0,0
    for pull in game.pulls:
        max_red = pull.colors['red'] if pull.colors['red'] > max_red else max_red
        max_green = pull.colors['green'] if pull.colors['green'] > max_green else max_green
        max_blue = pull.colors['blue'] if pull.colors['blue'] > max_blue else max_blue
    cube_powers_sum += max_red * max_green * max_blue

print(f'part 1: {possible_game_sum}')
print(f'part 2: {cube_powers_sum}')

