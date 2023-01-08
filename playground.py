import sys
sys.setrecursionlimit(10000)


N, K = [int(i) for i in input().strip().split()]
array = [int(i) for i in input().strip().split()]


def merge(arr, p, q, r):
    i = p
    j = q + 1
    t = 1
    tmp = [0 for _ in range(N)]
    while (i <= q and j <= r):
        if arr[i] <= arr[j]:
            tmp[t] = arr[i]
            t += 1
            i += 1
        else:
            tmp[t] = arr[j]
            t += 1
            j += 1
    while (i <= q):
        tmp[t] = arr[i]
        t += 1
        i += 1
    while (j <= r):
        tmp[t] = arr[j]
        t += 1
        j += 1
    i = p
    t = 1
    while (i <= r):
        arr[i] = tmp[t]
        i += 1
        t += 1


def merge_sort(arr, p, r):
    if p < r:
        q = (p+r)//2
        merge_sort(arr, p, q)
        merge_sort(arr, q+1, r)
        merge(arr, p, q, r)


merge_sort(array, 0, N-1)
# merge_sort(A[p..r]) { # A[p..r]을 오름차순 정렬한다.
# if (p < r) then {
#     q <- ⌊(p + r) / 2⌋;       # q는 p, r의 중간 지점
# merge_sort(A, p, q);      # 전반부 정렬
# merge_sort(A, q + 1, r);  # 후반부 정렬
# merge(A, p, q, r);        # 병합
# }
# }
#


