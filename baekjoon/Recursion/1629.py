# 곱셈
from sys import stdin


def solution(a, b, c, tmp, remains):
    for _ in range(b):
        tmp *= a
        remain = tmp % c
        if remain in remains:
            remains.append(remain)
            return True, remains[1:]
        remains.append(remain)
    return False, remains


A, B, C = map(int, stdin.readline().strip().split())
remains = []

is_repeat, remains = solution(A, B, C, 1, remains)
if is_repeat is True:
    print(remains[B % len(remains) - 2])
else:
    print(remains[-1])

print(remains)
print(A**B % C)
