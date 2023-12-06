import file_ops
from timer import TimeHandler
import re


def get_beat_count(time, distance_to_beat):
    beats = 0
    vertex = (time / 2) ** 2
    print(f' vertex: {vertex}')
    running_total = 1
    time_difference_count = 1
    while vertex >= distance_to_beat:
        running_total += 2
        vertex -= running_total
        time_difference_count += 1
    print(f'throw away times that are >= {time_difference_count}ms away from peak')
    focused_min, focused_max = int(time / 2 - time_difference_count + 1), int(time / 2 + time_difference_count)
    focused_max -= 1 if vertex % 1 != 0 else 0
    return focused_max - focused_min
    # brute force:
    # for hold_time in range(focused_min, focused_max):
    #     distance = (time - hold_time) * hold_time
    #     beats += 1 if distance > distance_to_beat else 0
    #     # print(f'hold for {hold_time} ms =  {distance} mm')
    # print(f'total beats: {beats}')
    # return beats


input_lines = file_ops.read_input(6)
timer = TimeHandler()

int_regex = re.compile(r'\d+')
times = [int(n) for n in int_regex.findall(input_lines[0])]
distances = [int(n) for n in int_regex.findall(input_lines[1])]

part2_time = int(f''.join([str(time) for time in times]))
part2_distance = int(f''.join([str(distance) for distance in distances]))

total_beats = 1
for i, time in enumerate(times):
    total_beats *= get_beat_count(time, distances[i])

p2_total_beats = get_beat_count(part2_time, part2_distance)

print(f'Part 1 total beats: {total_beats}')
print(f'Part 2 total beats: {p2_total_beats}')
print(timer.fetch_time())  # 5.23 seconds


# Parabola equation: x^2 = -4ay + a
# y = a(x-h)^2 + k   (h, k is vertex.  a =  coefficient)
# time = 10, dist = 20
# vertex = x=5, y=25
# Vertex = time/2 **2
