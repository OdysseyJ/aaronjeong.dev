import sys
import math
input = sys.stdin.readline


def lower_bound(target):
    st, en = 0, n

    while st < en:
        mid = (st+en)//2
        if a[mid] >= target:
            en = mid
        else:
            st = mid + 1
    return st


n, m = map(int, input().split())
a = sorted([int(input()) for _ in range(n)])
ans = math.inf
for i in a:
    idx = lower_bound(i+m)
    if idx != n:
        ans = min(ans, abs(i-a[idx]))

print(ans)
