from collections import deque


def bfs(graph, x, y):
    # 이동할 방향
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    n = len(graph)
    m = len(graph[0])

    queue = deque([(x, y)])
    while queue:
        x, y = queue.popleft()
        if graph[x][y] != 0:
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue

                if graph[nx][ny] == 1:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx, ny))

    return graph[n - 1][m - 1]


graph = [
    [1, 0, 1, 0, 1, 0],
    [1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
]

print(bfs(graph, 0, 0))
