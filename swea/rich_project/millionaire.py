import sys
from collections import deque


sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    nums = input().split()
    nums = deque([int(i) for i in nums])
    profit = 0

    max_num = max(nums)
    while nums:
        num = nums.popleft()
        if max_num > num:
            profit += max_num - num
        elif nums and max_num == num:
            max_num = max(nums)

    print(f"#{test_case} {profit}")

