import file_ops


part_two = True
num_dict = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5,
            'six':6, 'seven':7, 'eight':8, 'nine':9}

input_lines = file_ops.read_input(1)
calibration_sum = 0
part_two_calibration = 0
for line in input_lines:
    digits = ''
    for i, c in enumerate(line):
        # break if int
        digit = int(c) if c.isdecimal() else None
        if digit:
            digits = c
            break
        elif part_two:  # check if you find a word starting here
            num_word = c
            for _, c2 in enumerate(line[i + 1:]):
                num_word += c2
                if num_word in num_dict:
                    digits = str(num_dict[num_word])
                    break
        if digits != '':
            break

    # reverse and go backwards for digit 2
    reversed_line = line[::-1]
    for j, c in enumerate(reversed_line):
        digit = int(c) if c.isdecimal() else None
        if digit:
            digits += c
            break
        elif part_two:  # check if you find a word starting here
            num_word = c
            for _, c2 in enumerate(reversed_line[j + 1:]):
                num_word += c2
                if num_word[::-1] in num_dict:
                    digits += str(num_dict[num_word[::-1]])
        if len(digits) > 1:
            break

    if part_two:
        part_two_calibration += int(digits)
    else:
        calibration_sum += int(digits)

print(f'part 1: {calibration_sum} \n part 2: {part_two_calibration}')

