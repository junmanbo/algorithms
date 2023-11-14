from collections import deque


def solution(maps):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    n = len(maps)
    m = len(maps[0])

    deq = deque()
    deq.append((0, 0))

    while deq:
        x, y = deq.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if maps[nx][ny] == 1:
                deq.append((nx, ny))
                maps[nx][ny] = maps[x][y] + 1

    answer = maps[n-1][m-1]
    if answer == 1:
        return -1

    return answer


maps = [
    [1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1],
    [0, 0, 0, 0, 1]
]

print(solution(maps))
