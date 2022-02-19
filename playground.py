import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline


class Node(object):
    left = None
    right = None
    value = None

    def __init__(self, **kwargs):
        self.value = kwargs.get("value", None)


def pre_order(in_start, in_end, post_start, post_end):
    if(in_start > in_end) or (post_start > post_end):
        return

    root = post_order[post_end]
    print(root, end=" ")

    left = positions[root] - in_start
    right = in_end - positions[root]

    # left
    pre_order(in_start, in_start+left-1, post_start, post_start+left-1)
    # right
    pre_order(in_end-right+1, in_end, post_end-right, post_end-1)


k = int(input())
in_order = [int(i) for i in input().split(" ")]
post_order = [int(i) for i in input().split(" ")]

positions = [0] * (k+1)
for i in range(k):
    positions[in_order[i]] = i

pre_order(0, k-1, 0, k-1)
print()