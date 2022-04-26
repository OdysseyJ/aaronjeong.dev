import sys
input = sys.stdin.readline

current = 0
result = 0
for i in range(10):
    _out, _in = map(int, input().split())
    current += _in
    current -= _out
    result = max(current, result)
print(result)
