from collections import deque


def solution(prices):
    prices = deque(prices)
    answer = [0] * len(prices)
    tmp = deque()
    for idx, price in enumerate(prices):
        while tmp and tmp[-1][0] > price:
            answer[tmp[-1][1]] = idx - tmp[-1][1]
            tmp.pop()
        tmp.append((price, idx))
    while True:
        idx = tmp.popleft()[1]
        if not tmp:
            break
        answer[idx] = tmp[-1][1] - idx

    return answer


p = [1, 2, 3, 2, 3]
# p = [5, 4, 3, 2, 1]
print(solution(p))
