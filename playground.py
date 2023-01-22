import sys

N, M = map(int, sys.stdin.readline().strip().split())
check = [False for _ in range(N+1)]
results = dict()


def bt(nums):
    if len(nums) == M:
        result = ""
        for n in sorted(nums):
            result += f"{n} "
        results[result] = 1
        return

    for i in range(1, N+1):
        if not check[i]:
            check[i] = True
            bt(nums + [i])
            check[i] = False
t