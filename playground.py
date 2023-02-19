# 4056
import copy
import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline

N = int(input().strip())


def is_square_valid(arr, x, y, n):
    x_start = ((x-1) // 3) * 3 + 1
    y_start = ((y-1) // 3) * 3 + 1
    d = {}
    for i in range(x_start, x_start + 3):
        for j in range(y_start, y_start + 3):
            target = arr[i][j]
            if target in d and target != 0:
                return False
            if target == n:
                return False
            d[target] = True
    return True


def is_vertical_valid(arr, x, y, n):
    d = {}
    for i in range(1, 10):
        target = arr[i][y]
        if target in d and target != 0:
            return False
        if target == n:
            return False
        d[target] = True
    return True


def is_horizontal_valid(arr, x, y, n):
    d = {}
    for i in range(1, 10):
        target = arr[x][i]
        if target in d and target != 0:
            return False
        if target == n:
            return False
        d[target] = True
    return True


def find(arr, remains):
    global found
    if found:
        return

    if not remains:
        for i in range(1, 10):
            for j in range(1, 10):
                print(arr[i][j], end="")
            print()
        found = True
        return

    for remain in remains:
        x, y = remain
        for i in range(1, 10):
            if not is_vertical_valid(arr, x, y, i):
                continue
            if not is_horizontal_valid(arr, x, y, i):
                continue
            if not is_square_valid(arr, x, y, i):
                continue
            arr[x][y] = i
            new_remain = copy.deepcopy(remains)
            new_remain.remove(remain)
            find(arr, new_remain)
            arr[x][y] = 0


for _ in range(N):
    boards = [[0 for _ in range(10)] for _ in range(10)]
    zeros = []
    for i in range(9):
        for j, c in enumerate(input().strip()):
            num = int(c)
            if num == 0:
                zeros.append((i+1, j+1))
            boards[i+1][j+1] = num
    found = False
    find(boards, zeros)
    if not found:
        print("Could not complete this grid.")
    print()
