import sys
input = sys.stdin.readline

idx = 0
total = 0
for i in range(1, 6):
    nums = map(int, input().split())
    if (current:= sum(nums)) > total:
        idx = i
        total = current
print(idx, total)