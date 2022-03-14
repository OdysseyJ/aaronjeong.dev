import sys
from collections import deque
sys.setrecursionlimit(10000)
input = sys.stdin.readline


dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def is_valid(x, y):
    return 0 <= x < n and 0 <= y < n


def spread(virus):
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    for (x, y) in virus:
        visited[y][x] = 0

    cnt = 1
    queue = deque(virus)
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            n_x = x + dx[i]
            n_y = y + dy[i]
            if is_valid(n_x, n_y) and visited[n_y][n_x] == -1 and board[n_y][n_x] != 1:
                visited[n_y][n_x] = visited[y][x] + 1
                cnt = max(cnt, visited[n_y][n_x])
                queue.append((n_x, n_y))

    for i in range(n):
        for j in range(n):
            if board[i][j] == 0 and visited[i][j] == -1:
                cnt = -1

    return cnt


def put_virus(virus):
    global result

    if len(virus) == m:
        temp = spread(virus)
        if temp != -1:
            if result == -1:
                result = temp
            else:
                result = min(result, temp)
        return

    for idx, (x, y) in enumerate(viruses):
        if not visited[idx]:
            virus.append((x, y))
            visited[idx] = True
            put_virus(virus)
            visited[idx] = False
            virus.pop()


n, m = map(int, input().split())
board = [[0 for _ in range(n)] for _ in range(n)]
result = -1
viruses = []

for i in range(n):
    line = [int(k) for k in input().split()]
    for j in range(n):
        board[i][j] = line[j]
        if line[j] == 2:
            viruses.append((j, i))

visited = [False for _ in range(len(viruses))]
put_virus([])
print(result)
