import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline


def post_order(pre_start, pre_end, in_start, in_end):
    if in_start > in_end or pre_start > pre_end:
        return

    root = pre_order[pre_start]
    root_inorder_idx = positions[root]

    post_order(pre_start+1, pre_end, in_start, root_inorder_idx)
    post_order(pre_start+1, pre_end, root_inorder_idx+1, in_end)


t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    pre_order = [int(i) for i in input().strip().split()]
    in_order = [int(i) for i in input().strip().split()]
    positions = [0 for _ in range(n+1)]
    for idx, order in enumerate(in_order):
        positions[order] = idx
    print(positions)
    # post_order(0, n-1, 0, n-1)