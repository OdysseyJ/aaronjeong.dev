import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    count = int(input())
    nums = map(int, input().split())
    print(sum(nums))
