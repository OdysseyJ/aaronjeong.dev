import sys
from collections import deque
input = sys.stdin.readline


def solve(start):
    queue = deque([start])
    while queue:
        top, step = queue.popleft()
        if 100-top <= 6:
            return step + 1
        if top > 100:
            continue
        if top in ladders:
            queue.append((ladders[top], step))
            continue
        if top in snakes:
            queue.append((snakes[top], step))

        possibles = [top + dice for dice in range(1, 7)]
        for possible in possibles:
            queue.append((possible, step+1))


n, m = map(int, input().strip().split())
ladders = {}
snakes = {}

for _ in range(n):
    x, y = map(int, input().strip().split())
    ladders[x] = y

for _ in range(m):
    u, v = map(int, input().strip().split())
    snakes[u] = v

print(solve((1, 0)))
