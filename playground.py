import sys
input = sys.stdin.readline

n = int(input())
nums = map(int, input().split())
dp = [0] * n

for idx, num in enumerate(nums):
    if num == 1:
        if idx == 0:
            dp[idx] = 1
        else:
            dp[idx] = dp[idx-1] + 1
print(sum(dp))
