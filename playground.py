import sys
input = sys.stdin.readline


def binary_search(target):
    st, en = 0, nb
    while st < en:
        mid = (st+en)//2
        if b[mid] >= target:
            en = mid
        else:
            st = mid + 1
    if st >= nb or b[st] != target:
        result.append(target)


na, nb = [int(i) for i in input().split()]
a = sorted([int(i) for i in input().split()])
b = sorted([int(i) for i in input().split()])
result = []
for el in a:
    binary_search(el)

print(len(result))
for i in result:
    print(i, end=" ")
