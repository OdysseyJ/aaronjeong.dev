import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline


def back_tracking(arr):
    if len(arr) == m:
        for i in arr:
            print(i, end=" ")
        print()
        return

    for num in nums:
        arr.append(num)
        back_tracking(arr)
        arr.pop()


n, m = map(int, input().split())
nums = sorted([int(i) for i in input().split()])
back_tracking([])
