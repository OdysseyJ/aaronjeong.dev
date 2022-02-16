import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline


def solve(N, start, to, via):
    if N == 1:
        print(f"{start} {to}")
        return
    solve(N-1, start, via, to)
    solve(1, start, to, via)
    solve(N-1, via, to, start)
    return


n = int(input())
dp = [0 for _ in range(n+1)]
dp[0] = 0
dp[1] = 1
for i in range(2, n+1):
    dp[i] = 2*dp[i-1]+1
print(dp[i])
if n <= 20:
    solve(n, '1', '3', '2')