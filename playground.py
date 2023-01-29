# # 1 : 절대값으로 정렬 후 이웃 원소 더하기
#
# N = int(input())
# nums = [int(i) for i in input().strip().split()]
# s_nums = sorted(nums, key=lambda x: (abs(x), x))
#
# _min = abs(s_nums[0] + s_nums[1])
# results = (s_nums[0], s_nums[1])
# for a, b in zip(s_nums, s_nums[1:]):
#     _sum = abs(a+b)
#     if _sum < _min:
#         _min = _sum
#         results = (a, b)
# print(*sorted(results))
#
#
# # 2 : 투포인터
#
# N = int(input())
# nums = [int(i) for i in input().strip().split()]
# s_nums = sorted(nums)
#
# l = 0
# r = N-1
# _min = abs(s_nums[l] + s_nums[r])
# results = (s_nums[l], s_nums[r])
#
# while abs(r-l) != 1:
#     l_sum = abs(s_nums[l+1] + s_nums[r])
#     r_sum = abs(s_nums[l] + s_nums[r-1])
#     if l_sum < r_sum:
#         l += 1
#         if _min > l_sum:
#             _min = l_sum
#             results = (s_nums[l], s_nums[r])
#     else:
#         r -= 1
#         if _min > r_sum:
#             _min = r_sum
#             results = (s_nums[l], s_nums[r])
#
# print(*results)


# 11728
n, m = [int(i) for i in input().strip().split(" ")]
a = [int(i) for i in input().strip().split(" ")]
b = [int(i) for i in input().strip().split(" ")]
i_a, i_b = 0, 0

result = []
for i in range(n+m):
    if i_a == len(a):
        result.append(b[i_b])
        i_b += 1
    elif i_b == len(b):
        result.append(a[i_a])
        i_a += 1
    elif a[i_a] < b[i_b]:
        result.append(a[i_a])
        i_a += 1
    else:
        result.append(b[i_b])
        i_b += 1

print(" ".join(map(str, result)))
