import sys
from collections import deque
input = sys.stdin.readline


def bfs(start):
    visited = [-1 for _ in range(v+1)]
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


v = int(input())
tree = [[] for _ in range(v+1)]
for i in range(v):
    line = [int(i) for i in input().strip().split()]
    n1 = line[0]
    for n2, w in zip(line[1::2], line[2::2]):
        tree[n1].append((n2, w))

node, _ = bfs(1)
node, dist = bfs(node)
print(dist)
