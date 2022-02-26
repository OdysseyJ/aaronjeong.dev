import sys
from collections import deque
input = sys.stdin.readline


def bfs(start):
    visited = [-1 for _ in range(n+1)]
    visited[start] = 0
    queue = deque([start])
    max_node, max_weight = 0, 0
    while queue:
        top_n = queue.popleft()
        for next_n, next_w in tree[top_n]:
            if visited[next_n] == -1:
                queue.append(next_n)
                visited[next_n] = visited[top_n] + next_w
                if max_weight < visited[next_n]:
                    max_node, max_weight = next_n, visited[next_n]

    return max_node, max_weight


n = int(input())
tree = [[] for _ in range(n+1)]
for i in range(n-1):
    p, c, w = map(int, input().strip().split())
    tree[p].append((c, w))
    tree[c].append((p, w))

node, _ = bfs(1)
node, dist = bfs(node)
print(dist)
