import file_ops
from timer import TimeHandler
import re


class Hail:
    def __init__(self, px:int, py:int, pz:int, vx:int, vy:int, vz:int):
        self.px, self.py, self.pz = px, py, pz
        self.vx, self.vy, self.vz = vx, vy, vz
        self.slope_2d = self.vy / self.vx


timer = TimeHandler()
input_lines = file_ops.read_input('24_test')
storm = []
int_reg = re.compile(r'-?\d+')
for line in input_lines:
    vals = int_reg.findall(line)
    storm.append(Hail(*[int(v) for v in vals]))

# linear function  y = mx + b
# slope = y/x
# figure out the # of cycles it takes to cross paths
# find b for both hails, offset ?
# If slopes are parallel, No intercept... unless they collide
# test_area = range(200000000000000, 400000000000001)
test_area = range(0, 10)
for i, h in enumerate(storm):
    for h2 in storm[i+1:]:
        # throw out parallels
        if h.slope_2d / abs(h.slope_2d) == h2.slope_2d / abs(h2.slope_2d):
            continue
        b = -(h.slope_2d * h.px - h.py)
        b2 = -(h2.slope_2d * h2.px - h2.py)
        print(b, b2)




print(timer.fetch_time())
