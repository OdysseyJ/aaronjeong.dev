import sys
input = sys.stdin.readline

odds = []
while True:
    try:
        num = int(input())
        if num%2 != 0:
            odds.append(num)
    except:
        break
if not odds:
    print(-1)
else:
    print(sum(odds))
    print(sorted(odds)[0])