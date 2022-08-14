
def measure_count(n: int):
    count = 0
    if n == 1:
        return 1
    for i in range(1, n):
        if i * i == n:
            return 2 * count + 1
        if i * i > n:
            break
        if n % i == 0:
            count += 1
    return 2 * count


def is_valid(n: int):
    return (measure_count(n) % 2) != 0


n = input()
nums = [int(n) for n in input().split(" ")]


while True:
    for idx, (before, after) in enumerate(zip(nums, nums[1:])):
        if before > after and is_valid(before*after):
            nums[idx], nums[idx+1] = after, before
