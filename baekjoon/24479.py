# 알고리즘 수업 - 깊이 우선 탐색1
# DFS

from sys import stdin
from collections import defaultdict

def dfs(V, E, R):
    visited = [0] * (V + 1)
    order = [0] * (V + 1)
    stack = [R]
    count = 1

    while stack:
        node = stack.pop()
        if visited[node] == 0:
            visited[node] = 1
            order[node] = count
            count += 1
            stack.extend(sorted(E[node], reverse=True))

    return order[1:]

N, M, R = map(int, stdin.readline().split())

# N, M, R = 5, 5, 1
# edges = [(1, 4), (1, 2), (2, 3), (2, 4), (3, 4)]

E = defaultdict(list)
for _ in range(M):
    u, v = map(int, stdin.readline().split())
    E[u].append(v)
    E[v].append(u)

result = dfs(N, E, R)
for i in result:
    print(i if i != 0 else "0")
