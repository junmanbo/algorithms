from typing import List
from collections import deque


def solution(priorities: List[int], location: int) -> int:
    priorities = deque(priorities)
    cnt = 0
    while True:
        tmp = priorities.popleft()

        if priorities and max(priorities) > tmp:
            priorities.append(tmp)
        else:
            cnt += 1
            if location == 0:
                break

        if location == 0:
            location = len(priorities) - 1
        else:
            location -= 1
    return cnt


pri = [1, 1, 9, 1, 1, 1]
loc = 0
print(solution(pri, loc))
