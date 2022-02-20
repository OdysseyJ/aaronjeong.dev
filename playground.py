import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline


def solve(n, start, end):
    if n == k:
        return
    d = start + int((end-start)/2)
    root = in_order[d]
    results[n].append(root)
    solve(n+1, start, d-1)
    solve(n+1, d+1, end)


k = int(input())
in_order = input().split()
results = [[] for _ in range(k)]
solve(0, 0, 2**k-1-1)
for result in results:
    print(" ".join(result))