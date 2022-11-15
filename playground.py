import math
import sys

input = sys.stdin.readline


def get_width(idx, n):
    parent_idx = idx // 2
    if parent_idx == 0:  # root
        return n
    parent_width = get_width(parent_idx, n)
    if parent_width == 1:
        return 0
    if parent_width % 2 != 0 and idx % 2 == 0:
        return get_width(parent_idx, n)//2 + 1
    else:
        return get_width(parent_idx, n)//2


tree = [0] * 1000000


def init(node, start, end):
    global hs
    if start == end:
        tree[node] = int(hs[start])
        return tree[node]
    else:
        tree[node] = min(init(node * 2, start, (start + end) // 2), init(node * 2 + 1, (start + end) // 2 + 1, end))
        return tree[node]

# 7 2 1 4 5 1 3 3
# 4 1000 1000 1000 1000
# 0


while line := input().strip():
    if line == "0":
        break
    else:
        _n, *hs = line.split()
        n = int(_n)
        init(1, 0, n-1)
        _max = 0
        max_length = int(math.log(n, 2))+1
        for idx in range(1, 2**max_length+1):
            width = get_width(idx, n)
            area = width * tree[idx]
            _max = max(_max, area)
        print(_max)
