import math
from collections import deque


def solution(progresses, speeds):
    answer = deque()
    max = 0
    cnt = 0
    for idx, progress in enumerate(progresses):
        period = math.ceil((100 - progress) / speeds[idx])
        if idx == 0:
            max = period
            cnt = 1
        elif period > max:
            answer.append(cnt)
            max = period
            cnt = 1
        else:
            cnt += 1
    answer.append(cnt)
    return answer


progresses = [93, 30, 55]
speeds = [1, 30, 5]

# progresses = [95, 90, 99, 99, 80, 99]
# speeds = [1, 1, 1, 1, 1, 1]

print(solution(progresses, speeds))
