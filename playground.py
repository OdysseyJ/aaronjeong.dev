import sys
sys.setrecursionlimit(10000)


N = int(input().strip())


def recursion(s, l, r, c):
    c += 1
    if l >= r: return 1, c
    elif s[l] != s[r]: return 0, c
    else: return recursion(s, l+1, r-1, c)


def isPalindrome(s):
    result, count = recursion(s, 0, len(s)-1, 0)
    print(result, count)


for i in range(N):
    line = sys.stdin.readline().strip()
    isPalindrome(line)
