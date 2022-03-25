import sys
input = sys.stdin.readline

n = int(input())
for i in range(2*n):
    for j in range(n):
        if j % 2 == 0:
            print("*" if i % 2 == 0 else " ", end="")
        else:
            print(" " if i % 2 == 0 else "*", end="")
    print()
