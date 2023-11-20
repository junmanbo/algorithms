# leetcode 문자열 뒤집기
from typing import List


# 내 풀이
class Solution:
    def reverseString_my(self, s: List[str]) -> None:  # runtime: 200ms
        tmp = s.copy()
        for i in range(len(tmp)):
            s[i] = tmp.pop()
        print(s)

    def reverseString_two_pointer(self, s: List[str]) -> None:  # runtime: 194ms
        left = 0
        right = len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        print(s)

    def reverseString_pythonic(self, s: List[str]) -> None:  # runtime: 179ms
        s.reverse()
        print(s)


s = ["h", "e", "l", "l", "o"]
Solution().reverseString_pythonic(s)

# list 를 뒤집을 때 reverse 를 사용하자
