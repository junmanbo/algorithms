# SW Expert Academy view 문제 풀이
import sys
sys.stdin = open("input.txt", "r")

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input()) # 건물의 개수
    heights = input().split() # 건물의 높이
    total = 0

    for idx, height in enumerate(heights):
        height = int(height)

        try:
            diff_1 = height - int(heights[idx-2])
        except IndexError:
            diff_1 = height+1
        try:
            diff_2 = height - int(heights[idx-1])
        except IndexError:
            diff_2 = height+1
        try:
            diff_3 = height - int(heights[idx+1])
        except IndexError:
            diff_3 = height+1
        try:
            diff_4 = height - int(heights[idx+2])
        except IndexError:
            diff_4 = height+1

        if diff_1 >= 0 and diff_2 >= 0 and diff_3 >= 0 and diff_4 >= 0:
            tmp = [diff_1, diff_2, diff_3, diff_4]
            total += min(tmp)

    print(f"#{test_case} {total}")

