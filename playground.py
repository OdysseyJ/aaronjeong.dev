import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    car_price = int(input())
    options_cnt = int(input())
    total_price = car_price
    for j in range(options_cnt):
        cnt, price = map(int, input().split())
        total_price += (cnt * price)
    print(total_price)
