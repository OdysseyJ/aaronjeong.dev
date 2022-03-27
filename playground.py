import sys
input = sys.stdin.readline

n = int(input())
printer = [[" " for _ in range(4*n-3)] for _ in range(2*n-1)]
gap = n-2

for i in range(n):
    printer[0][i] = "*"
    printer[0][i+n+(2*n-3)] = "*"
    printer[(2*n-1)-1][i] = "*"
    printer[(2*n-1)-1][i+n+(2*n-3)] = "*"

for i in range(n):
    printer[i][i] = "*"
    printer[i][i+n-1] = "*"
    printer[i][(4*n-3)-i-n] = "*"
    printer[i][(4*n-3)-i-1] = "*"

for i in range(n):
    printer[(2*n-1)-i-1][i] = "*"
    printer[(2*n-1)-i-1][i+n-1] = "*"
    printer[(2*n-1)-i-1][n+(2*n-3)-i] = "*"
    printer[(2*n-1)-i-1][n+n+(2*n-3)-i-1] = "*"

for line in printer:
    print("".join(line).rstrip())
