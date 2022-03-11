import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline


def back_tracking(arr):
    if len(arr) == m:
        if m == 1 and arr[0] not in duplicated:
            duplicated[arr[0]] = True
            print(arr[0])
        elif " ".join(arr) not in duplicated:
            result = " ".join(arr)
            duplicated[result] = True
            print(result)
        return

    for idx, num in enumerate(nums):
        if not visited[idx]:
            visited[idx] = True
            arr.append(str(num))
            back_tracking(arr)
            arr.pop()
            visited[idx] = False


n, m = map(int, input().split())
nums = sorted([int(i) for i in input().split()])
visited = [False for _ in range(n)]
duplicated = {}
back_tracking([])
