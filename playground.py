import sys
from collections import deque

input = sys.stdin.readline

# 6 5
# 1 1 0 1 1
# 0 1 1 0 0
# 0 0 0 0 0
# 1 0 1 1 1
# 0 0 1 1 1
# 0 0 1 1 1

# input
height, width = [int(i) for i in input().strip().split(" ")]
board = [[0 for _ in range(width)] for _ in range(height)]
visited = [[False for _ in range(width)] for _ in range(height)]
for h in range(height):
    line = input().strip().split(" ")
    for w, i in enumerate(line):
        board[h][w] = int(i)

# prepare
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque([(x, y)])
    visited[y][x] = True
    count = 1
    while queue:
        first = queue.popleft()
        _x, _y = first
        board[_y][_x] = 0
        for i in range(4):
            _dx = dx[i] + _x
            _dy = dy[i] + _y
            if _dx < 0 or _dy < 0 or _dx >= width or _dy >= height:
                continue
            if visited[_dy][_dx] or board[_dy][_dx] == 0:
                continue
            visited[_dy][_dx] = True
            count += 1
            queue.append((_dx, _dy))
    return count


max_size = 0
count = 0
for h in range(height):
    for w in range(width):
        if board[h][w] == 1:
            count += 1
            max_size = max(max_size, bfs(w, h))

print(count)
print(max_size)


