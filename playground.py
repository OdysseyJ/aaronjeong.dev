import sys
from collections import deque
input = sys.stdin.readline

N, K = [int(i) for i in input().split()]
visited = [-1 for _ in range(100001)]


def t_bfs():
    queue = deque([(N, 0)])
    while queue:
        p, t = queue.popleft()
        if p == K:
            return t
        for i in [p+1, p-1, p*2]:
            if not (0 <= i <= 100000):
                continue
            if visited[i] != -1:
                continue
            visited[i] = t+1
            queue.append((i, t+1))


def c_bfs(time: int):
    count = 0
    queue = deque([(N, 0)])
    while queue:
        p, t = queue.popleft()
        if t == time and p == K:
            count += 1
        if time <= t:
            continue
        for i in [p+1, p-1, p*2]:
            if not (0 <= i <= 100000):
                continue
            queue.append((i, t+1))
    return count


min_time = t_bfs()
count = c_bfs(min_time)
print(min_time)
print(count)
