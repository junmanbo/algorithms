import sys
from collections import deque
sys.stdin = open("input.txt", "r")


def find_max(num, depth, max_depth, cache):
    if depth == max_depth:
        return int(num)

    if num in cache and depth in cache[num]:
        return cache[num][depth]

    max_val = -1
    num_list = list(str(num))

    for i in range(len(num_list)):
        for j in range(i + 1, len(num_list)):
            num_list[i], num_list[j] = num_list[j], num_list[i]
            temp_num = int(''.join(num_list))
            temp_val = find_max(temp_num, depth + 1, max_depth, cache)

            if temp_val > max_val:
                max_val = temp_val

            num_list[i], num_list[j] = num_list[j], num_list[i]

    if num not in cache:
        cache[num] = {}
    cache[num][depth] = max_val

    return max_val


T = int(input())
for t in range(1, T + 1):
    num, max_depth = input().split()
    max_depth = int(max_depth)
    cache = {}
    print(f"#{t} {find_max(num, 0, max_depth, cache)}")
