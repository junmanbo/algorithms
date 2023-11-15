# 프로그래머스 최소 직사각형 문제


def solution(sizes):
    for size in sizes:
        if size[1] > size[0]:
            size[0], size[1] = size[1], size[0]
    max_0 = max(sizes, key=lambda x: x[0])[0]
    max_1 = max(sizes, key=lambda x: x[1])[1]
    return max_0 * max_1


sizes1 = [
    [60, 50],
    [30, 70],
    [60, 30],
    [80, 40],
]
# 4000

sizes2 = [
    [10, 7],
    [12, 3],
    [8, 15],
    [14, 7],
    [5, 15],
]
# 120

sizes3 = [
    [14, 4],
    [19, 6],
    [6, 16],
    [18, 7],
    [7, 11],
]
# 133

print(solution(sizes3))
