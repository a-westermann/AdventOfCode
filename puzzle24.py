import file_ops
from timer import TimeHandler
import re
import math


class Hail:
    def __init__(self, px:int, py:int, pz:int, vx:int, vy:int, vz:int):
        self.px, self.py, self.pz = px, py, pz
        self.vx, self.vy, self.vz = vx, vy, vz
        self.m_2d = self.vy / self.vx
        self.b = -(self.m_2d * self.px - self.py)


def matching_vector(px, py, mx, my, p2x, p2y) -> bool:
    dot_product = mx * (p2x - px) + my * (p2y - py)
    # print(dot_product)
    return dot_product > 0

def point_inside_bounds(px, py, bx_min, bx_max, by_min, by_max):
    return bx_min <= px <= bx_max and by_min <= py <= by_max


timer = TimeHandler()
# input_lines = file_ops.read_input('24_test')
input_lines = file_ops.read_input(24)
storm = []
int_reg = re.compile(r'-?\d+')
for line in input_lines:
    vals = int_reg.findall(line)
    storm.append(Hail(*[int(v) for v in vals]))
# linear function  y = mx + b
# set y's equal to each other & solve: m2x2 + b2 = mx + b  then plug value into x and solve
# m2x2 = mx + b - b2
# m2x2 - mx = b - b2
# x = (b - b2) / (m2 - m)
t_min, t_max = 200000000000000, 400000000000000
# t_min = -10
intersections = 0
for i, h in enumerate(storm):
    for h2 in storm[i+1:]:
        # throw out parallels - UNLESS they will cross same paths
        if h.m_2d / abs(h.m_2d) == h2.m_2d / abs(h2.m_2d) and h2.m_2d - h.m_2d != 0:
            # intersections += 1
            # pass
            continue
        if abs(h2.m_2d) - abs(h.m_2d) == 0:
            # lines directly run over each other. Check if one line is along the other line in correct direction
            match_1 = matching_vector(h.px, h.py, h.vx, h.vy, h2.px, h2.py)
            match_2 = matching_vector(h2.px, h2.py, h2.vx, h2.vy, h.px, h.py)
            print(match_1, match_2)
            if (match_1 and point_inside_bounds(h2.px, h2.py, t_min, t_max, t_min, t_max)) \
              or (match_2 and point_inside_bounds(h.px, h.py, t_min, t_max, t_min, t_max)):
                print(f'good for {h.m_2d}  {h2.m_2d}   {h.px / 100000000000} {h.py/ 100000000000} '
                      f'  {h2.px/ 100000000000} {h2.py/ 100000000000}')
                intersections += 1
                continue
            else:
                print(f'BAD for {h.m_2d}  {h2.m_2d}   {h.px / 100000000000} {h.py / 100000000000} '
                      f'  {h2.px / 100000000000} {h2.py / 100000000000}')
                print("Nope")
        # print(f'BAD for {h.m_2d}  {h2.m_2d}   {h.px} {h.py}')
        x = (h.b - h2.b) / (h2.m_2d - h.m_2d)  # set equations equal and solve for x
        # if x is outside the test range throw it out
        if not t_min <= x <= t_max:
            continue
        # plug x in and solve for y (either equation)
        y = h.m_2d * x + h.b
        if not t_min <= y <= t_max:
            continue
        # print(f'intersect @ {x} {y}')
        # ensure the intersection is 'forward' (along the same directional vector) as the line trajectories
        if matching_vector(h.px, h.py, h.vx, h.vy, x, y) and matching_vector(h2.px, h2.py, h2.vx, h2.vy, x, y):
            intersections += 1

print(f'Part 1: {intersections}')
print(timer.fetch_time())
