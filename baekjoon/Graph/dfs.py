def dfs(graph, visited, node):
    if not visited[node]:
        visited[node] = True
        print(node, end=" ")
        for i in graph[node]:
            dfs(graph, visited, i)
    return visited[1:]


graph = [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5],
         [3, 4], [7], [2, 6, 8], [1, 7]
         ]

visited = [False] * 9


print(dfs(graph, visited, 1))
