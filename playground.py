import sys
input = sys.stdin.readline

n, s = map(int, input().split())
nums = [int(i) for i in input().strip().split()]
min_, sum_ = 1000001, 0
st, en = 0, 0
while st <= en:
    if sum_ >= s:
        min_ = min(min_, en-st)
        sum_ -= nums[st]
        st += 1
    else:
        if en == n:
            break
        sum_ += nums[en]
        en += 1

print(0 if min_ == 1000001 else min_)
