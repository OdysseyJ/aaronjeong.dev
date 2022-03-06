input = sys.stdin.readline


# 높이가 h일때 적어도 m이상의 나무를 가져갈 수 있는가
def solve(h):
    res = 0
    for tree in trees:
        if tree-h > 0:
            res += tree-h
    return res >= m


def binary_search():
    st, en = 0, max(trees)
    res = 0
    while st < en:
        mid = (st+en)//2
        if solve(mid):
            res = mid
            st = mid + 1
        else:
            en = mid
    print(res)


n, m = map(int, input().split())
trees = [int(i) for i in input().split()]
binary_search()
