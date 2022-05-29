import sys
import math
input = sys.stdin.readline


def calc_degree(p1, p2):
    return abs(math.atan2(p1[1] - p2[1], p1[0] - p2[0]) * 180 / math.pi)


data = [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2)]

st = (1, 3)
point_degrees = [(p, calc_degree(p, st)) for p in data]
sorted_points = sorted(point_degrees, key=lambda x: x[1])

# def convex_hull():
#     stack = [st, sorted_points[0]]
#     while True:
#         pass
#
#
#