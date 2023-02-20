import sys

MAX = 1000000

DECIMAL = 1
NON_DECIMAL = 0
dp = [DECIMAL] * (MAX+1)
dp[1] = NON_DECIMAL
for i in range(2, MAX):
    if dp[i] == DECIMAL:
        for j in range(i*i, MAX+1, i):
            dp[j] = NON_DECIMAL


while True:
    n = int(sys.stdin.readline().strip())
    if n == 0:
        break
    for i in range(3, int(n/2)+1):
        if dp[i] == DECIMAL and dp[n-i] == DECIMAL:
            print("{} = {} + {}".format(n, i, n-i))
            break
        if i == int(n/2):
            print("Goldbach's conjecture is wrong")
            break
