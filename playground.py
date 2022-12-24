import sys
from collections import deque
input = sys.stdin.readline

# 5 17
# 2
# 17 5
# 4

MAX = 500000
n, k = [int(i) for i in input().strip().split()]
if n == k:
    print(0)
else:
    v_c = [-1 for _ in range(MAX+1)]
    v_s = [-1 for _ in range(MAX+1)]

    t_c = 0
    p_c = k
    while p_c <= MAX:
        v_c[p_c] = t_c
        t_c += 1
        p_c += t_c

    def bfs():
        t_s = 0
        temp = [n]
        while temp:
            queue = deque(temp)
            temp = []
            while queue:
                p_s = queue.popleft()
                for i in [p_s*2, p_s+1, p_s-1]:
                    if not (0 <= i <= MAX):
                        continue
                    n_t_s = t_s + 1
                    if v_c[i] == n_t_s:
                        print(n_t_s)
                        return
                    if n_t_s >= t_c:
                        continue
                    if v_s[i] == n_t_s:
                        continue
                    v_s[i] = n_t_s
                    temp.append(i)
            t_s += 1
        print(-1)

    bfs()