# 4056
import sys
input = sys.stdin.readline

N = int(input().strip())

def find_square():
    pass


def find_vertical():
    pass


def find_horizontal():
    pass


def find(arr, remains):
    if not remains:
        for i in range(1, 10):
            for j in range(1, 10):
                print(arr[i][j])
    for remain in remains:
        x, y = remain

        # 가능한 리스트 뽑기
        possible = 5
        find_square()
        find_vertical()
        find_horizontal()

        arr[x][y] = possible
        visited[x][y] = True
        next_remains = remain.remove(remain)
        find(arr, next_remains)
        visited[x][y] = False


for _ in range(N):
    boards = [[0 for _ in range(10)] for _ in range(10)]
    visited = [[False for _ in range(10)] for _ in range(10)]
    zeros = []
    for i in range(9):
        for j, c in enumerate(input().strip()):
            num = int(c)
            if num == 0:
                zeros.append((i, j))
            boards[i+1][j+1] = num
