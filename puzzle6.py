import file_ops
from timer import TimeHandler
import re


input_lines = file_ops.read_input(6)
timer = TimeHandler()

int_regex = re.compile('\d+')
times = int_regex.findall(input_lines[0])
distances = int_regex.findall(input_lines[1])

for i, time in enumerate(times):
    distance = 0
    print(time)
    for hold_time in range(1, time):   # don't need to evaluate value at 0/100% of race time
        distance = (time - hold_time) * hold_time
        print(f'hold for {hold_time} ms =  {distance} mm')

    break

print(timer.fetch_time())
