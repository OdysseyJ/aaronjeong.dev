# 4056
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N = int(input().strip())


def is_square_valid(arr, x, y, i):
    pass


def is_vertical_valid(arr, x, y, i):
    pass


def is_horizontal_valid(arr, x, y, i):
    pass


def find(arr, remains):
    if not remains:
        for i in range(1, 10):
            for j in range(1, 10):
                print(arr[i][j])

    for remain in remains:
        x, y = remain

        # 가능한 리스트 뽑기
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
            remains.add(remain)


for _ in range(N):
    boards = [[0 for _ in range(10)] for _ in range(10)]
    zeros = []
    for i in range(9):
        for j, c in enumerate(input().strip()):
            num = int(c)
            if num == 0:
                zeros.append((i, j))
            boards[i+1][j+1] = num
    find(boards, zeros)
