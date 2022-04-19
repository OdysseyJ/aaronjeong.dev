import sys
input = sys.stdin.readline

primes = [True for _ in range(10001)]
primes[1] = False

for i, is_prime in enumerate(primes):
    if i in [0, 1]:
        continue
    if is_prime:
        for j in range(i*i, 10001, i):
            primes[j] = False

m = int(input())
n = int(input())

total = 0
min_num = 0
for i in range(m, n+1):
    if primes[i]:
        total += i
        if not min_num:
            min_num = i

if total:
    print(total)
    print(min_num)
else:
    print(-1)
