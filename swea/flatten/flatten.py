# SW Expert Academy 평탄화 문제

import sys

sys.stdin = open("input.txt", "r")


def solution(n, heights):
    for _ in range(n):
        max_height = max(heights)
        min_height = min(heights)

        check_max_height = False
        check_min_height = False

        for idx, height in enumerate(heights):
            if check_max_height is False and height == max_height:
                heights[idx] -= 1
                check_max_height = True
            elif check_min_height is False and height == min_height:
                heights[idx] += 1
                check_min_height = True
            elif check_min_height is True and check_max_height is True:
                break

    max_height = max(heights)
    min_height = min(heights)

    return max_height - min_height


T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    heights = input().split()
    heights = [int(height) for height in heights]
    print(f"#{test_case} {solution(n, heights)}")
