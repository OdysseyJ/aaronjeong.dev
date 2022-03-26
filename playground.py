import sys
input = sys.stdin.readline

n = int(input())
printer = [[" " for _ in range(4*n-3)] for _ in range(4*n-1)]

if n == 1:
    print("*")
else:
    for i in range(n):
        start = 2*i
        width = 4*(n-i)-3
        height = 4*(n-i)-1
        for j in range(start, start+width):
            printer[start][j] = "*"
        for j in range(start, start+width):
            printer[start+height-1][j] = "*"
        for j in range(start, start+height):
            printer[j][start] = "*"
        for j in range(start+2, start+height):
            printer[j][start+width-1] = "*"
        if i != 0:
            printer[start][start+width] = "*"

    for idx, line in enumerate(printer):
        print("".join(line).strip())
