import sys
input = sys.stdin.readline

nums = []
while True:
    try:
        num = int(input())
        nums.append(num)
    except:
        print(sum(nums))
        break
