import file_ops
from timer import TimeHandler


def rotate_platform_clockwise(platform: list[str]) -> list[str]:
    # could use platform.reversed() to be more memory efficient vs. shallow copy
    rotated = zip(*platform[::-1])
    rotated = [''.join([a for a in r]) for r in rotated]
    # [print(r) for r in rotated]
    return rotated
    # return [str(a) for a in list(zip(*platform[::-1]))]
    # return list(zip(*platform[::-1]))


def tilt(platform: list[str]) -> list[str]:
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
# for x in rotate_platform_clockwise(input_lines):
#     pass

tilted_platform = input_lines
tilted_platform = tilt(tilted_platform)
total_load = 0
for r, row in enumerate(tilted_platform):
    # print(row)
    for char in row:
        if char == 'O':
            total_load += len(tilted_platform) - r

print(f'Total load: {total_load}')
# Part 2:
cycles = 1000000000
for i in range(cycles):
    if i > 0:
        tilted_platform = tilt(rotate_platform_clockwise(tilted_platform))
    for j in range(3):
        tilted_platform = tilt(rotate_platform_clockwise(tilted_platform))
        # print('\n\n')
        # [print(x) for x in tilted_platform]
    if i % 10 == 0:
        print(f'cycle: {i}')


print(timer.fetch_time())  # 0.03 seconds
