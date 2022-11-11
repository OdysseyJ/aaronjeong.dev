import sys

input = sys.stdin.readline

line = input().strip()

stack = []
result = 0
prev = None
for char in line:
    if char == "(":
        stack.append(char)
    elif char == ")":
        stack.pop()
        if prev == ")":
            result += 1
        else:
            result += len(stack)
    prev = char
print(result)

import sys

# input = sys.stdin.readline
#
# line = input().strip()
#
# stack = []
# result = 0
# for char in line:
#     if char == ")":
#         num = 0
#         while top := stack.pop() != "(":
#             num += top
#         num = 2 * num if num else 2
#         stack.append(num)
#     elif char == "]":
#         num = 0
#         while top := stack.pop() != "[":
#             num += top
#         num = 3 * num if num else 3
#         stack.append(num)
#     else:
#         stack.append(char)
#
#
