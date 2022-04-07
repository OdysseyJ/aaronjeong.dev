import sys
input = sys.stdin.readline

n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    print(f'Case {i+1}: {a+b}')
