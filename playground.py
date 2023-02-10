# 4056
import copy
import sys
from pprint import pprint

sys.setrecursionlimit(10000)
input = sys.stdin.readline

N = int(input().strip())


def is_square_valid(arr, x, y, n):
    # 0 0 0 0 0 0 0 0 0 0
    # 0 1 2 3 4 5 6 7 8 9
    # 0 2 3 4 5 6 7 8 9 1
    # 0 3 4 5 6 7 8 9 1 2
    # 0 3 4 5 6 7 8 9 1 2
    # 0 3 4 5 6 7 8 9 1 2
    # 0 3 4 5 6 7 8 9 1 2
    # 0 3 4 5 6 7 8 9 1 2

    x_start = ((x-1) // 3) * 3 + 1
    y_start = ((y-1) // 3) * 3 + 1

    for i in range(x_start, x_start + 3):
        for j in range(y_start, y_start + 3):
            if arr[i][j] == n:
                return False
    return True


def is_vertical_valid(arr, x, y, n):
    for i in range(1, 10):
        if arr[i][y] == n:
            return False
    return True


def is_horizontal_valid(arr, x, y, n):
    for i in range(1, 10):
        if arr[x][i] == n:
            return False
    return True


def find(arr, remains):
    if not remains:
        for i in range(1, 10):
            for j in range(1, 10):
                print(arr[i][j], end="")
            print()

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
            remains.remove(remain)
            find(arr, remains)
            arr[x][y] = 0
            remains.remove(remain)


for _ in range(N):
    boards = [[0 for _ in range(10)] for _ in range(10)]
    zeros = []
    for i in range(9):
        for j, c in enumerate(input().strip()):
            num = int(c)
            if num == 0:
                zeros.append((i+1, j+1))
            boards[i+1][j+1] = num
    find(boards, zeros)
