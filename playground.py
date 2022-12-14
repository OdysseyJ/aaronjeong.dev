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
board = []
visited = [[False for _ in range(width)] for _ in range(height)]
for h in range(height):
    board.append([int(i) for i in input().strip().split(' ')])

print(board)
print(visited)

# prepare
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque([(x, y)])
    visited[y][x] = True
    count = 1
    while queue:
        first = queue.popleft()
        for i in range(4):
            x = first[0]
            y = first[1]
            _dx = dx[i] + x
            _dy = dy[i] + y
            if _dx < 0 or _dy < 0 or _dx >= width or _dy >= height:
                continue
            if visited[_dy][_dx] or board[_dy][_dx] == 0:
                continue
            visited[_dy][_dx] = True
            board[y][x] = 0
            count += 1
            queue.append((_dx, _dy))
    return count


for line in board:
    for num in board:
        if num == 1:
            pass
            # bfs(x, y)
        else:
            continue


