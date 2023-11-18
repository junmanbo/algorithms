# SW Expert Academy 달팽이 숫자

import sys

sys.stdin = open("input.txt", "r")


def get_snail_number(n, answer):
    # 우하좌상
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    controll = 0

    cnt = 0
    i = 0
    j = 0
    while cnt < n * n:
        cnt += 1
        answer[i][j] = cnt

        nx = i + dx[controll]
        ny = j + dy[controll]

        if nx < 0 or ny < 0 or nx >= n or ny >= n or answer[nx][ny] != 0:
            controll += 1
            if controll == 4:
                controll = 0

        i += dx[controll]
        j += dy[controll]
    return answer


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    answer = [[0] * n for _ in range(n)]
    answer = get_snail_number(n, answer)
    print(f"#{test_case}")
    for i in range(n):
        for j in range(n):
            print(answer[i][j], end=" ")
        print()
