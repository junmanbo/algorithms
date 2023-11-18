# leetcode 유효한 팰린드롬


class Solution:
    def isPalindrome(self, s: str) -> bool:
        tmp = []
        for i in s:
            if i.isalpha() or i.isalnum():
                tmp.append(i.lower())
        print(tmp)
        return tmp == tmp[::-1]


string = "A man, a plan, a canal: Panama"
string2 = "race a car"
string3 = "0P"

print(Solution().isPalindrome(string3))
