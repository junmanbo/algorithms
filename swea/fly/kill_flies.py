# SW Expert Academy 파리 퇴치

import sys

sys.stdin = open("input.txt", "r")


def kill_fly(n, m, flies):
    start_location = [0, 0]
    end_location = [m, m]

    kill_max = 0

    while True:
        kill_total = 0
        for i in range(start_location[0], end_location[0] + 1):
            for j in range(start_location[1], end_location[1] + 1):
                kill_total += flies[i][j]
        if kill_total > kill_max:
            kill_max = kill_total

        if end_location[0] == n - 1 and end_location[1] == n - 1:
            return kill_max
        elif end_location[1] + 1 >= n:
            start_location[0] += 1
            end_location[0] += 1
            start_location[1] = 0
            end_location[1] = m
        else:
            start_location[1] += 1
            end_location[1] += 1


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    flies = []
    for i in range(n):
        tmp = input().split()
        tmp = [int(j) for j in tmp]
        flies.append(tmp)
    print(f"#{test_case} {kill_fly(n, m - 1, flies)}")
