import file_ops
from timer import TimeHandler


input_lines = file_ops.read_input(6)
timer = TimeHandler()


print(timer.fetch_time())
