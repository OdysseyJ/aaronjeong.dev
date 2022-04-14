import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    print(2-a+b)

# 2
# 8 12
# 4 6
