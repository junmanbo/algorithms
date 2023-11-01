# 음료수 얼려먹기 문제


def dfs(graph, n, m, x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(graph, n, m, x - 1, y)
        dfs(graph, n, m, x + 1, y)
        dfs(graph, n, m, x, y - 1)
        dfs(graph, n, m, x, y + 1)
        return True
    return False


# n은 세로길이, m은 가로길이
n, m = 4, 5

# 0 -> 구멍 O
# 1 -> 구멍 X
graph = [[0, 0, 1, 1, 0], [0, 0, 0, 1, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0]]

cnt = 0
for i in range(n):
    for j in range(m):
        if dfs(graph, n, m, i, j) is True:
            cnt += 1
print(cnt)
