import file_ops
from timer import TimeHandler
import re


def calc_differences(numbers: list[list[int]]) -> list[list[int]]:
    lower_tier = []
    for i, n in enumerate(numbers[-1][0:len(numbers[-1]) - 1]):
        next_diff = numbers[-1][i + 1] - n
        lower_tier.append(next_diff)
    numbers.append(lower_tier)
    if len([n for n in lower_tier if n != 0]) > 0:
        return calc_differences(numbers)
    return numbers


def extrapolate(number_tiers: list[list[int]], last_number: bool) -> int:
    number_tiers.reverse()
    index = -1 if last_number else 0
    for i in range(1, len(number_tiers)):
        tier = number_tiers[i]
        if last_number:
            tier.append(tier[-1] + number_tiers[i - 1][-1])
        else:
            tier.insert(0, tier[0] - number_tiers[i - 1][0])
        print(tier)
        if tier == number_tiers[-1]:
            return tier[index]


timer = TimeHandler()
input_lines = file_ops.read_input(9)
int_regex = re.compile(r'-?\d+')
sequences = []
p1_total, p2_total = 0, 0
for line in input_lines:
    input_sequence = list(map(int, int_regex.findall(line)))
    sequences.append(input_sequence)
    tiers = calc_differences([input_sequence])
    p2_tiers = tiers.copy()
    p1_total += extrapolate(tiers, True)
    p2_total += extrapolate(p2_tiers, False)


print(f'Part 1: {p1_total}')
print(f'Part 2: {p2_total}')
print(timer.fetch_time())  # 0.07 seconds
