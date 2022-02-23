import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline


def solve(n, x, y):
    if n == 1:
        printer[y][x] = "*"
        return

    # 가로 한줄
    for n_x in range(x, x+dp_w[n]):
        printer[y][n_x] = "*"

    half = int(x+dp_w[n]/2)

    if n % 2 == 0:
        # 대각선
        for idx, n_x in enumerate(range(x, half)):
            printer[y+idx][n_x] = "*"
        for idx, n_x in enumerate(range(half, x+dp_w[n])):
            printer[y+dp_h[n]-idx-1][n_x] = "*"
        solve(n-1, x+int(dp_w[n-1]/2)+2, y+dp_h[n-1])

    if n % 2 == 1:
        # 대각선
        for idx, n_x in enumerate(range(x, half)):
            printer[y-idx][n_x] = "*"
        for idx, n_x in enumerate(range(half, x+dp_w[n])):
            printer[y-dp_h[n]+idx+1][n_x] = "*"
        solve(n-1, x+int(dp_w[n-1]/2)+2, y-dp_h[n-1])


n = int(input())
dp_w = [0 for _ in range(n+1)]
dp_h = [0 for _ in range(n+1)]
dp_w[1] = 1
dp_h[1] = 1
for i in range(2, n+1):
    dp_w[i] = 2*dp_w[i-1] + 3
    dp_h[i] = 2*dp_h[i-1] + 1
printer = [[" " for _ in range(dp_w[n]+1)] for _ in range(dp_h[n])]

if n % 2 == 0:
    solve(n, 0, 0)
    for idx, y in enumerate(range(dp_h[n])):
        for x in range(dp_w[n]-idx):
            print(printer[y][x], end="")
        print()
else:
    solve(n, 0, dp_h[n]-1)
    for idx, y in enumerate(range(dp_h[n])):
        for x in range(dp_w[n]-dp_h[n]+idx+1):
            print(printer[y][x], end="")
        print()
