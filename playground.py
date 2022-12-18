import sys
from collections import deque

input = sys.stdin.readline

# 4 6
# 101111
# 101010
# 101011
# 111011

# input
height, width = [int(i) for i in input().strip().split(" ")]
board = [[0 for _ in range(width)] for _ in range(height)]
visited = [[False for _ in range(width)] for _ in range(height)]
for h in range(height):
    line = input().strip()
    for w, i in enumerate(line):
        board[h][w] = int(i)
        visited[h][w] = False if int(i) == 1 else True

# prepare
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
target = (width - 1, height - 1)

queue = deque([(0, 0, 0)])
visited[0][0] = True
while queue:
    first = queue.popleft()
    _x, _y, step = first
    target_x, target_y = target
    if target_x == _x and target_y == _y:
        print(step+1)
        break
    for i in range(4):
        _dx = dx[i] + _x
        _dy = dy[i] + _y
        if _dx < 0 or _dy < 0 or _dx >= width or _dy >= height:
            continue
        if visited[_dy][_dx]:
            continue
        next_step = step + 1
        visited[_dy][_dx] = True
        queue.append((_dx, _dy, next_step))
