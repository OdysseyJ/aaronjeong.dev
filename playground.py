import sys
input = sys.stdin.readline

sentence = input().strip()

size = ord('z') - ord('a')
array = [0 for _ in range(size+1)]
a = ord('a')
for s in sentence:
    idx = ord(s) - a
    array[idx] += 1
for i in array:
    print(i, end=" ")
