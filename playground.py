import sys
input = sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)]

def counting_sort(arr):
    freq = [0 for _ in range(2000001)]

    for num in nums:
        freq[1000000+num] += 1

    for idx, i in enumerate(freq):
        if i != 0:
            for j in range(i):
                print(idx-1000000)