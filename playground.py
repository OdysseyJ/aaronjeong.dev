import sys
input = sys.stdin.readline


n = int(input())
dp = [0 for _ in range(20)]

for i in range(n):
    t, p = map(int, input().split(" "))
    # 오늘이 내일보다 큰 경우 내일 오늘까지 수익 채우기
    if dp[i] > dp[i+1]:
        dp[i+1] = dp[i]
    # t일 후의 수익이 현재 수익+p보다 더 작을경우 업데이트
    if dp[i+t] < dp[i]+p:
        dp[i+t] = dp[i]+p

print(dp[n])
