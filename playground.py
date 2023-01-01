import sys
from collections import deque
input = sys.stdin.readline

N, K = [int(i) for i in input().split()]
visited = [-1 for _ in range(100001)]


cnt = 0
queue = deque([(N, 0)])
visited[N] = 0
while queue:
    p, t = queue.popleft()
    if p == K:
        cnt += 1
    for i in [p+1, p-1, p*2]:
        if not (0 <= i <= 100000):
            continue
        if visited[i] != -1 and visited[i] <= visited[p]:
            continue
        visited[i] = t+1
        queue.append((i, t+1))
print(visited[K])
print(cnt)
