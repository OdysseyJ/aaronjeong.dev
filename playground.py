import sys
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def upd(x, y, direction):
    direction %= 4
    while True:
        x += dx[direction]
        y += dy[direction]
        if is_invalid(x, y) or board2[x][y] == 6:
            return
        if board2[x][y] != 0:
            continue
        board2[x][y] = 7


def is_invalid(x, y):
    return x < 0 or x >= n or y < 0 or y >= m


n, m = map(int, input().split())
board1 = [[0 for _ in range(10)] for _ in range(10)]
board2 = [[0 for _ in range(10)] for _ in range(10)]
cctvs = []
min_ = 0

for i in range(n):
    line = [int(k) for k in input().split()]
    for j in range(m):
        board1[i][j] = line[j]
        if line[j] not in [0, 6]:
            cctvs.append((i, j))
        if line[j] == 0:
            min_ += 1

# CCTV 4방향 탐색
for t in range(4**len(cctvs)):
    for i in range(n):
        for j in range(m):
            board2[i][j] = board1[i][j]
    brute = t
    for i in range(len(cctvs)):
        # 일의 자리 가져오기 - 각 cctv별 방향 구하기 가능
        direction = brute % 4
        # 자릿수 하나 내려주기 - 다음 cctv방향 탐색을 위해
        brute = int(brute/4);

        x, y = cctvs[i]
        if board1[x][y] == 1:
            upd(x, y, direction)
        elif board1[x][y] == 2:
            upd(x, y, direction)
            upd(x, y, direction+2)
        elif board1[x][y] == 3:
            upd(x, y, direction)
            upd(x, y, direction+1)
        elif board1[x][y] == 4:
            upd(x, y, direction)
            upd(x, y, direction+1)
            upd(x, y, direction+2)
        elif board1[x][y] == 5:
            upd(x, y, direction)
            upd(x, y, direction+1)
            upd(x, y, direction+2)
            upd(x, y, direction+3)

    cur = 0
    for i in range(n):
        for j in range(m):
            if board2[i][j] == 0:
                cur += 1
    min_ = min(min_, cur)
print(min_)
