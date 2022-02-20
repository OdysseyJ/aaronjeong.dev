import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline


def solve(num, n):
    sum_ = sum([int(n) for n in num])
    if len(num) == 1:
        print(n)
        print("YES" if sum_ % 3 == 0 else "NO")
        return
    solve(str(sum_), n+1)


num = input().strip()
solve(num, 0)