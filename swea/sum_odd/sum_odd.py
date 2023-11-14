import sys

sys.stdin = open("input.txt", "r")

T = int(input())

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    total = 0
    nums = input().split(" ")
    print(nums)
    for num in nums:
        num = int(num)
        if num % 2 == 1:
            total += num
    print(total)
