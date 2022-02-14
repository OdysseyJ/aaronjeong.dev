import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline


def solve(n, x, y):
    if n == 1:
        p = paper[y][x]
        counts[p] += 1
        return p
    div = int(n/3)
    p1 = solve(div, x, y)
    p2 = solve(div, x+div, y)
    p3 = solve(div, x+div+div, y)
    p4 = solve(div, x, y+div)
    p5 = solve(div, x+div, y+div)
    p6 = solve(div, x+div+div, y+div)
    p7 = solve(div, x, y+div+div)
    p8 = solve(div, x+div, y+div+div)
    p9 = solve(div, x+div+div, y+div+div)
    if p1 is not None and p1 == p2 == p3 == p4 == p5 == p6 == p7 == p8 == p9:
        counts[p1] -= 8
        return p1


n = int(input().strip())
paper = [[0 for _ in range(n)] for _ in range(n)]
counts = [0 for _ in range(3)]

for i in range(n):
    line = list(map(int, input().strip().split(" ")))
    for j, c in enumerate(line):
        paper[i][j] = c

solve(n, 0, 0)
for i in [-1, 0, 1]:
    print(counts[i])
