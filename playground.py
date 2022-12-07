import math
import sys

input = sys.stdin.readline

# 7 2 1 4 5 1 3 3
# 4 1000 1000 1000 1000
# 0


while line := input().strip():
    if line == "0":
        break
    else:
        _n, *hs = [int(i) for i in line.split()]
        stack = []
        _max = 0
        for idx, h in enumerate(hs):
            width = 1
            while stack and hs[stack[-1]] >= h:
                top = stack.pop()
                _max = max(_max, width * hs[top])
                width += 1
            stack.append(idx)
        while stack:
            top = stack.pop()
            if stack:
                width = _n - stack[-1] - 1
            else:
                width = _n
            _max = max(_max, width * hs[top])
        print(_max)
