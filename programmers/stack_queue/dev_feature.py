import math
from collections import deque


def solution(progresses_val, speeds_val):
    answer = deque()
    max_val = 0
    cnt = 0
    for idx, progress in enumerate(progresses_val):
        period = math.ceil((100 - progress) / speeds_val[idx])
        if idx == 0:
            max_val = period
            cnt = 1
        elif period > max_val:
            answer.append(cnt)
            max_val = period
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
