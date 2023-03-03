import sys
input = sys.stdin.readline

n = int(input().strip())

# dp[i][n] = n번째 칸까지 최대(0~2), 최소(3~5)
dp = [[0 for _ in range(6)] for _ in range(n)]

arr = []
for i in range(n):
    nums = [int(i) for i in input().strip().split(" ")]
    a, b, c = nums
    if i == 0:
        dp[i][0] = nums[0]
        dp[i][1] = nums[1]
        dp[i][2] = nums[2]
        dp[i][3] = nums[0]
        dp[i][4] = nums[1]
        dp[i][5] = nums[2]
    else:
        dp[i][0] = max(dp[i-1][0] + nums[0], dp[i-1][1] + nums[0])
        dp[i][1] = max(dp[i-1][0] + nums[1], dp[i-1][1] + nums[1], dp[i-1][2] + nums[1])
        dp[i][2] = max(dp[i-1][1] + nums[2], dp[i-1][2] + nums[2])

        dp[i][3] = min(dp[i-1][3] + nums[0], dp[i-1][4] + nums[0])
        dp[i][4] = min(dp[i-1][3] + nums[1], dp[i-1][4] + nums[1], dp[i-1][5] + nums[1])
        dp[i][5] = min(dp[i-1][4] + nums[2], dp[i-1][5] + nums[2])

max_r = max(dp[n-1][:3])
min_r = min(dp[n-1][3:])
print(max_r, min_r)
