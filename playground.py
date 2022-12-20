import sys
from collections import deque

input = sys.stdin.readline

height, width = [int(i) for i in input().strip().split(" ")]
j = (0, 0)
fires = []
board = [[1001 for _ in range(width)] for _ in range(height)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for h in range(height):
    line = input().strip()
    for w, i in enumerate(line):
        if i == "#":
            board[h][w] = -1
        elif i == "F":
            fires.append((w, h))
            board[h][w] = 1
        elif i == "J":
            j = (w, h)


def fbfs():
    queue = deque(fires)
    while queue:
        _x, _y = queue.popleft()
        for i in range(4):
            _dx = dx[i] + _x
            _dy = dy[i] + _y
            if not (0 <= _dx < width and 0 <= _dy < height):
                continue
            if board[_dy][_dx] != 1001:
                continue
            board[_dy][_dx] = board[_y][_x] + 1
            queue.append((_dx, _dy))


def hbfs():
    queue = deque([j])
    j_x, j_y = j
    board[j_y][j_x] = 1
    while queue:
        _x, _y = queue.popleft()
        for i in range(4):
            _dx = dx[i] + _x
            _dy = dy[i] + _y
            if not (0 <= _dx < width and 0 <= _dy < height):
                print(board[_y][_x])
                return
            if board[_dy][_dx] <= board[_y][_x] + 1:
                continue
            board[_dy][_dx] = board[_y][_x] + 1
            queue.append((_dx, _dy))
    print("IMPOSSIBLE")
    return


fbfs()
hbfs()
