import file_ops


# class SchematicItem:
#     def __init__(self, row: int, columns: list[int]):
#         self.row = row
#         self.columns = columns
#
# class PartNumber(SchematicItem):
#     def __init__(self, row: int, columns: list[int], part_number: int):
#         super(PartNumber, self).__init__(row, columns)
#         self.part_number = part_number

input_lines = file_ops.read_input(3)
part_number_sum = 0

# row,index set containing symbol positions
symbol_positions: {(int, int)} = {}
for r, line in enumerate(input_lines):
    c = 0
    for _ in range(len(line)):
        char = line[c]
        number = char
        char_skip = 1  # to know length of part number digits
        if char.isdecimal():
            char_index = c + 1
            while char_index < len(line) and line[char_index].isdecimal():
                number += line[char_index]
                char_index += 1
            # Completed part number. Check for surrounding symbols
            for i in range(r - 1, r + 2):
                if i < 0 or i >= len(input_lines):
                    continue  # outside bounds of input
                for j in range(c - 1, c + len(number) + 2):
                    if (i == r and (j != c - 1 or j != c + 1)) or (j < 0 or j >= len(line)):
                        continue  # on the part number or out of bounds of line
                    item = input_lines[i][j]
                    if item != '.' and not item.isdecimal():  # safety
                        print(number)
                        part_number_sum += int(number)
                        char_skip = len(number)
                        break
                if char_skip > 1:
                    break
        c += char_skip
        if c >= len(line):
            break

print(part_number_sum)
