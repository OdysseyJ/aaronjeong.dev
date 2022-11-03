import sys
input = sys.stdin.readline

n = int(input().strip())
nums = [int(i) for i in input().strip().split(" ")]
x = int(input().strip())

array = [0 for _ in range(x+1)]
result = 0
for num in nums:
    target = x-num
    if target < 0:
        continue
    if array[target] == 1:
        result += 1
    else:
        array[num] = 1
print(result)
