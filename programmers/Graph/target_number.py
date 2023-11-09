def solution(numbers, target):
    if not numbers:
        return 1 if target == 0 else 0
    else:
        return solution(numbers[1:], target - numbers[0]) + solution(
            numbers[1:], target + numbers[0]
        )


# numbers = [1, 1, 1, 1, 1]
# target = 3
numbers = [4, 1, 2, 1]
target = 4

print(solution(numbers, target))
