import sys
import math
input = sys.stdin.readline


def lower_bound(t):
    st, en = 0, n
    while st < en:
        mid = (st+en)//2
        if waters[mid] >= t:
            en = mid
        else:
            st = mid + 1
    return st


def binary_search():
    rst, ren = math.inf, math.inf
    for idx, water in enumerate(waters):
        # -water에 대한 lower_bound를 구한다.
        complement_idx = lower_bound(-water)

        # water[i]와 더했을 때 값이 가장 작은 원소 : water[i+1] / water[i] / water[i-1]
        if n > complement_idx+1 != idx and abs(rst + ren) > abs(waters[idx] + waters[complement_idx+1]):
            rst, ren = waters[idx], waters[complement_idx+1]
        if n > complement_idx != idx and abs(rst + ren) > abs(waters[idx] + waters[complement_idx]):
            rst, ren = waters[idx], waters[complement_idx]
        if n > complement_idx-1 != idx and abs(rst + ren) > abs(waters[idx] + waters[complement_idx-1]):
            rst, ren = waters[idx], waters[complement_idx-1]

    rst, ren = sorted([rst, ren])
    print(f'{rst} {ren}')


n = int(input())
waters = sorted([int(i) for i in input().split()])
binary_search()
