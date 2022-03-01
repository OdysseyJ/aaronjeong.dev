import sys
input = sys.stdin.readline

n = int(input())
cards = [int(input()) for _ in range(n)]
MAX = 2**62

sorted_cards = sorted(cards)
sorted_cards = sorted_cards + [MAX+1]

cnt = 1
max_cnt = 0
max_val = -MAX-1
for prev, next in zip(sorted_cards, sorted_cards[1:]):
    if prev == next:
        cnt += 1
    else:
        if cnt > max_cnt:
            max_cnt = cnt
            max_val = prev
        cnt = 1

print(max_val)
