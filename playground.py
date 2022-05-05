import sys
input = sys.stdin.readline

n = int(input())
for i in range(n):
    num = int(input())
    idx = 0
    while True:
        if num == 0:
            break
        if num % 2 == 1:
            print(idx, end=" ")
        num = int(num / 2)
        idx += 1
    print()
