import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    print(f"You get {a // b} piece(s) and your dad gets {a % b} piece(s).")
