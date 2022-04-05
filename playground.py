import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * 50
dp[1] = 1
for i in range(2, 50):
    dp[i] = dp[i-1] + dp[i-2]
print(dp[n])