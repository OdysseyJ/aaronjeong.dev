import sys
input = sys.stdin.readline

n = int(input())
for i in range(n):
    if i == n-1:
        for j in range(2*i+1):
            print("*", end="")
    else:
        for j in range(n-i-1):
            print(" ", end="")
        print("*", end="")
        for j in range(2*i-1):
            print(" ", end="")
        if 2*i-1 > 0:
            print("*", end="")
    print()