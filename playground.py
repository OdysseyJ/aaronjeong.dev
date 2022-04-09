import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    m = int(input())
    _max = 0
    result = ""
    for i in range(m):
        price, name = input().split()
        if _max < int(price):
            _max = max(_max, int(price))
            result = name
    print(result)
