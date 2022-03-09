import sys
from collections import deque
input = sys.stdin.readline

move = [(-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]


def is_valid(x, y):
    return 0 <= x < n and 0 <= y < n


def bfs(start):
    queue = deque([start])

    while queue:
        x, y = queue.popleft()
        if x == r2 and y == c2:
            return visited[x][y]
        for m_x, m_y in move:
            new_x, new_y = x+m_x, y+m_y
            if is_valid(new_x, new_y) and visited[new_x][new_y] == 0:
                visited[new_x][new_y] = visited[x][y] + 1
                queue.append((new_x, new_y))
    return -1


n = int(input())
r1, c1, r2, c2 = map(int, input().split())
visited = [[0 for _ in range(n)] for _ in range(n)]
print(bfs((r1, c1)))
