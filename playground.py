import sys
input = sys.stdin.readline
n = int(input().strip())
nums = map(int, input().strip().split())
sorted_nums = sorted(nums)
dp = [0 for _ in range(n)]
dp[0] = sorted_nums[0]

for idx, num in enumerate(sorted_nums[1:]):
  dp[idx+1] = dp[idx] + num

print(sum(dp))