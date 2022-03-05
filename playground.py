import sys
input = sys.stdin.readline


def binary_search(target):
    st, en = 0, n
    while st < en:
        mid = (st+en)//2
        if cards[mid] >= target:
            en = mid
        else:
            st = mid + 1
    if st < n and cards[st] == target:
        return 1
    else:
        return 0


n = int(input())
cards = sorted([int(i) for i in input().split()])
m = int(input())
targets = [int(i) for i in input().split()]

for target in targets:
    print(binary_search(target), end=" ")
