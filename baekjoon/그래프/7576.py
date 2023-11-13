from collections import deque
from sys import stdin

input = stdin.readline

def get_rotten(tomato_box, n, m):
    rotten_tomato = deque()
    for i in range(n):
        for j in range(m):
            if tomato_box[i][j] == 1:
                rotten_tomato.append((i, j))
    return rotten_tomato

def bfs(tomato_box, n, m, rotten_tomatos):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    x, y = 0, 0

    total_rotten = len(rotten_tomatos)

    deq = deque()
    for rotten_tomato in rotten_tomatos:
        x, y = rotten_tomato
        deq.append((x, y))

    while deq:
        x, y = deq.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m or tomato_box[nx][ny] == -1:
                continue

            if tomato_box[nx][ny] == 0:
                deq.append((nx, ny))
                tomato_box[nx][ny] = tomato_box[x][y] + 1
                total_rotten += 1

    for tomato_row in tomato_box:
        if 0 in tomato_row:
            return -1

    return tomato_box[x][y] - 1


tomato_box = []
m, n = map(int, input().strip().split())
for _ in range(n):
    tmp = input().strip().split()
    tmp = [int(i) for i in tmp]
    tomato_box.append(tmp)

rotten_tomatos = get_rotten(tomato_box, n, m)
print(bfs(tomato_box, n, m, rotten_tomatos))


