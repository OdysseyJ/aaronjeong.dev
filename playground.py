import sys
sys.setrecursionlimit(10000)


N = int(input().strip())
paper = [[0 for _ in range(N)] for _ in range(N)]
counts = [0 for _ in range(3)]

for i in range(N):
    line = [int(i) for i in input().strip().split()]
    for j, c in enumerate(line):
        paper[i][j] = c


def solve(n, x, y):
    if n == 1:
        num = paper[x][y]
        counts[num] += 1
        return num

    d = n//3
    t0 = solve(d, x, y)
    t1 = solve(d, x+d, y)
    t2 = solve(d, x+d+d, y)
    t3 = solve(d, x, y+d)
    t4 = solve(d, x+d, y+d)
    t5 = solve(d, x+d+d, y+d)
    t6 = solve(d, x, y+d+d)
    t7 = solve(d, x+d, y+d+d)
    t8 = solve(d, x+d+d, y+d+d)

    if t0 is not None and t0 == t1 == t2 == t3 == t4 == t5 == t6 == t7 == t8:
        counts[t0] -= 8
        return t0


solve(N, 0, 0)
for i in [-1, 0, 1]:
    print(counts[i])
