import sys
input = sys.stdin.readline


def lower_index(target):
    start = 0
    end = n

    while start < end:
        mid = int((start+end)/2)
        if a_array[mid] >= target:
            end = mid
        else:
            start = mid + 1
    return start


def upper_index(target):
    start = 0
    end = n

    while start < end:
        mid = int((start+end)/2)
        if a_array[mid] > target:
            end = mid
        else:
            start = mid + 1
    return start


n = int(input())
a_array = sorted([int(i) for i in input().strip().split()])
m = int(input())
candidates = [int(i) for i in input().strip().split()]

for candidate in candidates:
    print(upper_index(candidate) - lower_index(candidate))