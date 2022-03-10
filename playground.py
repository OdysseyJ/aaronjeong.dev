import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def is_valid(x, y):
    return 0 <= x < m and 0 <= y < n


def spread():
    global max_

    queue = deque(viruses)
    new_board = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            new_board[i][j] = board[i][j]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            n_x = x + dx[i]
            n_y = y + dy[i]
            if is_valid(n_x, n_y) and new_board[n_y][n_x] == 0:
                queue.append((n_x, n_y))
                new_board[n_y][n_x] = 2

    cnt = 0
    for i in range(n):
        for j in range(m):
            if new_board[i][j] == 0:
                cnt += 1

    max_ = max(max_, cnt)


def build_wall(cnt):
    if cnt == 3:
        spread()
        return

    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                board[i][j] = 1
                build_wall(cnt+1)
                board[i][j] = 0


n, m = map(int, input().split())
board = [[0 for _ in range(m)] for _ in range(n)]
viruses = []
max_ = -1
for i in range(n):
    line = map(int, input().strip().split())
    for j, el in enumerate(line):
        board[i][j] = el
        if el == 2:
            viruses.append((j, i))
build_wall(0)
print(max_)
