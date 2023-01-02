import sys
input = sys.stdin.readline

_dx = [-1, 0, 1, 0]
_dy = [0, -1, 0, 1]


N = int(input().strip())
arr = []
for i in range(N):
    arr.append([int(j) for j in input().strip().split()])


def dfs(height):
    cnt = 0
    visited = [[False for _ in range(N)] for _ in range(N)]
    for x in range(N):
        for y in range(N):
            if visited[x][y] or arr[x][y] < height:
                continue
            cnt += 1
            stack = [(x, y)]
            visited[x][y] = True
            while stack:
                _x, _y = stack.pop()
                for idx in range(4):
                    dx = _dx[idx] + _x
                    dy = _dy[idx] + _y
                    if not (0<=dx<N) or not (0<=dy<N):
                        continue
                    if visited[dx][dy] == True:
                        continue
                    if arr[dx][dy] < height:
                        continue
                    visited[dx][dy] = True
                    stack.append((dx, dy))
    return cnt


count = 0
for h in range(1, 101):
    count = max(dfs(h), count)
print(count)
