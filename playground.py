import sys
input = sys.stdin.readline


def remove_dup(array):
    array = array + [10**9+1]
    result = []
    for prev, next in zip(array, array[1:]):
        if prev != next:
            result.append(prev)
    return result


def binary_search(array, target):
    start, end = 0, len(array)
    while start < end:
        mid = (start+end) // 2
        if array[mid] >= target:
            end = mid
        else:
            start = mid + 1
    return start


n = int(input())
x = [int(i) for i in input().strip().split()]


non_duplicated_sorted = remove_dup(sorted(x))
for el in x:
    print(binary_search(non_duplicated_sorted, el), end=" ")
