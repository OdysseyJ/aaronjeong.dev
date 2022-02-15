import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline


def solve(n, x, y):
    if n == 1:
        p = paper[y][x]
        counts[p] += 1
        return p
    div = int(n/2)
    p1 = solve(div, x, y)
    p2 = solve(div, x+div, y)
    p3 = solve(div, x, y+div)
    p4 = solve(div, x+div, y+div)
    if p1 is not None and p1 == p2 == p3 == p4:
        counts[p1] -= 3
        return p1


n = int(input().strip())
paper = [[0 for _ in range(n)] for _ in range(n)]
counts = [0 for _ in range(2)]

for i in range(n):
    line = list(map(int, input().strip().split(" ")))
    for j, c in enumerate(line):
        paper[i][j] = c

solve(n, 0, 0)
for i in [0, 1]:
    print(counts[i])
