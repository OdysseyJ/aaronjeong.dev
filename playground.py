import sys
input = sys.stdin.readline


# 막대 과자 길이가 t일때 m조각 이상 나오나
def solve(t):
    if t == 0:
        return True
    return sum([i//t for i in l]) >= m


def binary_search():
    st, en = 1, max(l)

    res = 0
    while st <= en:
        mid = (st+en)//2
        if solve(mid):
            res = mid
            st = mid+1
        else:
            en = mid-1
    print(res)


m, n = [int(i) for i in input().split()]
l = [int(i) for i in input().split()]
binary_search()