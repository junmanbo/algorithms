import sys

sys.stdin = open("input.txt", "r")

N = int(input())

nums = input().split(" ")
nums.sort()
med = N // 2 - 2
print(med)

print(nums[med])
