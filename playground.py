import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline


def w(a, b, c):
    if dp[a][b][c] != 0:
        return dp[a][b][c]
    if a <= 0 or b <= 0 or c <= 0:
        dp[a][b][c] = 1
    elif a > 20 or b > 20 or c > 20:
        dp[a][b][c] = w(20, 20, 20)
    elif a < b < c:
        dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    else:
        dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    return dp[a][b][c]


dp = [[[0 for _ in range(101)] for _ in range(101)] for _ in range(101)]

while True:
    a, b, c = map(int, input().strip().split(" "))
    if a == b == c == -1:
        break
    w(a, b, c)
    print(f"w({a}, {b}, {c}) = {dp[a][b][c]}")