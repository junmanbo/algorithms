from typing import List
from collections import deque


def solution(bridge_length: int, weight: int, truck_weights: List[int]) -> int:
    truck_weights = deque(truck_weights)
    crossing = deque([])
    current_time = 0
    while truck_weights or crossing:
        if crossing and current_time - crossing[0][1] == bridge_length:
            crossing.popleft()
        if truck_weights:
            truck = truck_weights.popleft()
            total_crossing = 0
            for crossing_weight in crossing:
                total_crossing += crossing_weight[0]  # 다리 건너고 있는 트럭들의 무게
            total_crossing += truck
            crossing_length = len(crossing)
            if total_crossing <= weight and crossing_length < bridge_length:
                crossing.append([truck, current_time])
            else:
                truck_weights.appendleft(truck)
        current_time += 1
    return current_time


# # case1
# bridge_length = 2
# weight = 10
# truck_weights = [7, 4, 5, 6]

# # case2
# bridge_length = 100
# weight = 100
# truck_weights = [10]

# case3
bridge_length = 100
weight = 100
truck_weights = [10] * 10

print(solution(bridge_length, weight, truck_weights))
