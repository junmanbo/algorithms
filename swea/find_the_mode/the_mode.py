# SW Expert Academy 최빈수 구하기
from collections import Counter

import sys

sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    nums = Counter(input().split())
    max_freq_nums = max(nums.values())
    freq_nums = [int(k) for k, v in nums.items() if v == max_freq_nums]
    print(f"#{n} {max(freq_nums)}")
