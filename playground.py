import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    m = int(input())
    _sum = 0
    _sum_gpa = 0
    for i in range(m):
        a, b = map(float, input().split())
        _sum += a
        _sum_gpa += a*b
    print(int(_sum), round(_sum_gpa/int(_sum), 1))
