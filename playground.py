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
                    if n_t_s == v_s[i]:  # 같은 시간초 에서 중복 큐 삽입 막기
                        continue
                    v_s[i] = n_t_s
                    arr.append(i)
            t_s += 1
        print(-1)
        # if v_s[k] != -1:  # 수빈이가 한번 이라도 그 장소에 간적 있으면
        #     print(t_s)
        # else:  # Not Found
        #     print(-1)

    bfs()
