import sys
input = sys.stdin.readline


origin = "ABABABADABABACABAD"
target = "ABABACABA"


def fail():
    # FIXME : implement
    return [0, 0, 1, 2, 3, 0, 1, 2, 3]


def kmp():
    _fail = fail()
    i, j = 0, 0
    while i != len(origin):
        if origin[i] == target[j]:
            i += 1
            j += 1
        else:
            if j-1 < 0:
                i += 1
                j = 0
            else:
                j = _fail[j-1]

        if j == len(target):
            print("find")
            j = _fail[j-1]


kmp()
