import sys
from collections import deque

input = sys.stdin.readline
MAX = 500000
n, k = [int(i) for i in input().strip().split()]
v_s = [[-1 for _ in range(MAX+1)] for _ in range(2)]


def bfs():
    v_s[0][n] = 0
    queue = deque([(n, 0)])
    while queue:
        p_s, t_s = queue.popleft()
        n_t_s = t_s + 1
        flag = t_s % 2
        for i in [p_s*2, p_s+1, p_s-1]:
            if not (0 <= i <= MAX):
                continue
            if v_s[1-flag][i] != -1:
                continue
            v_s[1-flag][i] = n_t_s
            queue.append((i, n_t_s))


bfs()

t_c = 0
p_c = k
result = -1
while p_c <= MAX:
    if v_s[t_c % 2][p_c] != -1 and v_s[t_c % 2][p_c] <= t_c:
        result = t_c
        break
    t_c += 1
    p_c += t_c
print(result)
