import sys
input = sys.stdin.readline

n = int(input())
dots = sorted([int(i) for i in [input().split() for _ in range(n)]], key=lambda d: (d[0], d[1]))

for (x, y) in dots:
    print(f"{x} {y}")
