import sys


res = set()


def solve(orig, brackets, removes, cur):
    if cur == len(brackets):
        if removes:
            reversed_removes = reversed(sorted(removes))
            temp = orig

            for r in reversed_removes:
                temp = temp[0: r] + temp[r+1:]
            res.add(temp)
        return

    solve(orig, brackets, removes, cur + 1)
    solve(orig, brackets, removes + brackets[cur], cur + 1)


x = sys.stdin.readline().strip()
stack = []
brackets = []

for i, char in enumerate(x):
    if char == '(':
        stack.append(i)
    elif char == ')':
        brackets.append([stack.pop(), i])

solve(x, brackets, [], 0)
print(*sorted(list(res)), sep='\n')
