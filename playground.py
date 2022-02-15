import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline


def solve(n, x, y):
    if n == 3:
        for i, j in [(0, 0), (-1, 1), (1, 1), (-2, 2), (-1, 2), (0, 2), (1, 2), (2, 2)]:
            paper[y+j][x+i] = "*"
        return
    div = int(n/2)
    solve(div, x, y)
    solve(div, x-div, y+div)
    solve(div, x+div, y+div)


n = int(input().strip())
paper = [[" " for _ in range(2*n-1)] for _ in range(n)]

solve(n, int((2*n-1)/2), 0)
for l in paper:
    print("".join(l))