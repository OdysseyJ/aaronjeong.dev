import sys
input = sys.stdin.readline


origin = "ABABABADABABACABABAD"

s = "ABABACABABA"
# ABABACABABA
# 00123012343

# i = 5
# j = 3


def fail():
    f = [0 for _ in range(len(s))]
    j = 0
    for i in range(1, len(s)):
        while j > 0 and s[i] != s[j]:
            j = f[j-1]
        if s[i] == s[j]:
            j += 1
            f[i] = j
    return f


def kmp():
    _fail = fail()
    i, j = 0, 0

    while i != len(origin):
        if origin[i] == s[j]:
            i += 1
            j += 1
        else:
            if j-1 < 0:
                i += 1
                j = 0
            else:
                j = _fail[j-1]

        if j == len(s):
            print("find")
            j = _fail[j-1]


kmp()
