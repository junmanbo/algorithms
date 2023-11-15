# 프로그래머스 모의고사 문제
from collections import deque


def solution(answers):
    results = [0] * 3

    nums0 = deque([1, 2, 3, 4, 5])
    nums1 = deque([2, 1, 2, 3, 2, 4, 2, 5])
    nums2 = deque([3, 3, 1, 1, 2, 2, 4, 4, 5, 5])

    for answer in answers:
        num0 = nums0.popleft()
        num1 = nums1.popleft()
        num2 = nums2.popleft()

        if num0 == answer:
            results[0] += 1
        if num1 == answer:
            results[1] += 1
        if num2 == answer:
            results[2] += 1

        nums0.append(num0)
        nums1.append(num1)
        nums2.append(num2)

    max_result = max(results)
    return [idx + 1 for idx, result in enumerate(results) if max_result == result]


answers = [1, 2, 3, 4, 5]
# [1]

answers = [1, 3, 2, 4, 2]
# [1, 2, 3]

print(solution(answers))
