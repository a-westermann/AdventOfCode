import file_ops
from timer import TimeHandler

# If part 2 is rotate different ways, just rotate the actual input
def tilt(direction: (int, int), platform: list[str]) -> list[str]:
    # code here to rotate the input based on the direction
    new_layout = []
    for r, line in enumerate(platform):
        new_layout.append('')
        for i, rock in enumerate(line):
            row_index = r
            while rock == '.':  # shift lower rocks up
                if row_index + 1 == len(platform) or\
                        platform[row_index + 1][i] == '#':
                    break
                rock = platform[row_index + 1][i]
                platform[row_index + 1] = platform[row_index + 1][:i] + '.' +\
                    platform[row_index + 1][i + 1:]
                row_index += 1
            # line = line[:i] + rock + line[i+1:]
            new_layout[-1] += rock
        # break
    return new_layout


timer = TimeHandler()
input_lines = file_ops.read_input(14)
tilted_platform = tilt((0, 1), input_lines)
for t in tilted_platform:
    print(t)

print(timer.fetch_time())