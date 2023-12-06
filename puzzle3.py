import file_ops


def get_number(row: str, char_index: int) -> str:  # part 1 method
    part_number = ''
    while char_index < len(row) and row[char_index].isdecimal():
        part_number += line[char_index]
        char_index += 1
    return part_number


input_lines = file_ops.read_input(3)
part_number_sum = 0
gear_ratio = 0

for r, line in enumerate(input_lines):
    c = 0
    while c < len(line):
        char = line[c]
        char_skip = 1  # to know length of part number digits for part 1

        # ____PART 2______
        if char == '*':
            gear_nums = []
            for i in range(r - 1, r + 2):
                if i < 0 or i >= len(input_lines):
                    continue  # outside bounds of input
                j = (c - 1)
                following_char_count = 1
                while j < c + 2:
                    if j < 0 or j >= len(line):
                        continue  # out of bounds
                    item = input_lines[i][j]
                    gear_num = item
                    if item.isdecimal():
                        # check if end of number
                        prev_char = j - 1
                        # print(f' found {gear_num}')
                        while prev_char >= 0 and input_lines[i][prev_char].isdecimal():
                            gear_num = input_lines[i][prev_char] + gear_num
                            prev_char -= 1
                        # check if start of number
                        next_char = j + 1
                        while next_char < len(line) and input_lines[i][next_char].isdecimal():
                            gear_num = gear_num + input_lines[i][next_char]
                            next_char += 1
                            following_char_count += 1
                        gear_nums.append(gear_num)

                    if len(gear_nums) > 2:
                        break
                    j += following_char_count
                if len(gear_nums) > 2:
                    break
            if len(gear_nums) == 2:
                # valid gear. multiply them together
                gear_ratio += (int(gear_nums[0]) * int(gear_nums[1]))

        # ____PART 1______
        elif char.isdecimal():
            finished_analyzing = False
            number = get_number(line, c)
            # Completed part number. Check for surrounding symbols
            char_skip = len(number)
            for i in range(r - 1, r + 2):
                if i < 0 or i >= len(input_lines):
                    continue  # outside bounds of input
                for j in range(c - 1, c + len(number) + 1):
                    if (i == r and (j != c - 1 and j != c + len(number))) or (j < 0 or j >= len(line)):
                        continue  # on the part number or out of bounds of line
                    item = input_lines[i][j]
                    if item != '.' and not item.isdecimal():  # safety
                        part_number_sum += int(number)
                        finished_analyzing = True
                        break
                if finished_analyzing:
                    break
        c += char_skip
        if c >= len(line):
            break

print(f' Part 1 : {part_number_sum}')
print(f' Part 2 : {gear_ratio}')
