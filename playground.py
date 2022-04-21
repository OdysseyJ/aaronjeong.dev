import sys
input = sys.stdin.readline

n = int(input())

total = 0
for i in range(n+1):
    total += int((3*i*(i+1))/2)

print(total)
