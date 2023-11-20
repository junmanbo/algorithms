# https://leetcode.com/problems/most-common-word/
import re
from collections import Counter, defaultdict
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        for char in paragraph:
            if not char.isalpha():
                # ,나 . 같은 기호가 연속으로 붙어서 있는 경우 바로 split을 사용하면 안 나누어짐
                paragraph = paragraph.replace(char, " ")
        n_paragraph = paragraph.split()
        count_word = {}
        for word in n_paragraph:
            word = word.lower()
            if word in banned:
                continue
            elif word in count_word:
                count_word[word] += 1
            else:
                count_word[word] = 1

        return max(count_word.items(), key=lambda x: x[1])[0]

    # Counter 사용
    def mostCommonWord_simple(self, paragraph: str, banned: List[str]) -> str:
        words = [
            word
            for word in re.sub(r"[^\w]", " ", paragraph).lower().split()
            if word not in banned
        ]
        counts = Counter(words)
        return counts.most_common(1)[0][0]


# paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
paragraph = "a, a, a, a, b,b,b,c, c"
banned = ["a"]

print(Solution().mostCommonWord_simple(paragraph, banned))
