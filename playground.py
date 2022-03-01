target = [6, -8, 1, 12, 8, 3, 7, -7]


def quick_sort(array):
    if len(array) == 1:
        return array
    pivot = 0
    l, r = 1, len(array)-1
    while l <= r:
        print(l, r)
        if array[l] < array[pivot]:
            l += 1
            continue
        if array[r] > array[pivot]:
            r -= 1
            continue
        array[l], array[r] = array[r], array[l]
    array[pivot], array[r] = array[r], array[pivot]

    left = quick_sort(array[:r+1])
    right = quick_sort(array[r+1:])

    return left+right


def quick_sort_2(target, st, en):
    if en <= st+1:
        return
    pivot = st
    l, r = st+1, en-1
    while l <= r:
        print(l, r)
        if target[l] < target[pivot]:
            l += 1
            continue
        if target[r] > target[pivot]:
            r -= 1
            continue
        target[l], target[r] = target[r], target[l]
    target[pivot], target[r] = target[r], target[pivot]

    quick_sort_2(target, st, r)
    quick_sort_2(target, r+1, en)


quick_sort_2(target, 0, len(target))
print(target)