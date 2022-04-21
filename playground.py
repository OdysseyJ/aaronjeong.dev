import sys
input = sys.stdin.readline

n = int(input())

nums = [int(input()) for _ in range(n)]
print(sum(nums)-(n-1))

# n-1만큼 빼기
# 3
# 1
# 1
# 1