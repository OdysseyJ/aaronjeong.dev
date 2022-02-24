S = input()
T = input()
found = False


def solve(ss):
    global found
    if len(ss) < len(S):
        return
    if ss == S:
        found = True
        return

    if ss[0] == 'B':
        ss = ss[::-1]
        ss = ss[:-1]
        solve(ss)
        ss = ss + 'B'
        ss = ss[::-1]

    if ss[-1] == 'A':
        ss = ss[:-1]
        solve(ss)


solve(T)
print(1 if found else 0)