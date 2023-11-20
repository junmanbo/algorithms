from collections import deque


def bfs(graph, visited, node):
    queue = deque([node])
    visited[node] = True
    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for i in graph[node]:
            if visited[i] is False:
                visited[i] = True
                queue.append(i)

    return visited[1:]


graph = [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]

visited = [False] * 9


print(bfs(graph, visited, 1))
