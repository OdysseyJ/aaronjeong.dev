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
    v_s = [[-1 for _ in range(MAX+1)] for _ in range(2)]

    t_c = 0
    p_c = k
    while p_c <= MAX:
        v_c[p_c] = t_c
        t_c += 1
        p_c += t_c

    def bfs():
        t_s = 0
        arr = [n]
        while arr:
            if t_s > t_c:  # 수빈이가 동생 보다 더 오래 걸리는 경우
                break

            queue = deque(arr)
            arr = []
            while queue:
                p_s = queue.popleft()
                for i in [p_s*2, p_s+1, p_s-1]:
                    if not (0 <= i <= MAX):  # 범위 체크
                        continue
                    n_t_s = t_s + 1
                    if n_t_s == v_c[i]:  # 정답
                        print(n_t_s)
                        return
                    if v_s[1-(t_s % 2)][i] != -1:
                        continue
                    v_s[1-(t_s % 2)][i] = n_t_s
                    arr.append(i)
            t_s += 1
        print(-1)

    bfs()
