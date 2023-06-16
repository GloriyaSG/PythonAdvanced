from collections import deque


def best_list_pureness(nums, K):
    rotation = K
    nums = deque(nums)
    max_sum = float("-inf")
    cycle = 0
    for rotating in range(rotation+1):
        indexing = []
        for index, num in enumerate(nums):
            indexing.append((index,num))
        sum_rotations = 0
        for key, value in indexing:
            sum_rotations += (key*value)
        if sum_rotations > max_sum:
            max_sum = sum_rotations
            cycle = rotating
        nums.rotate()
    return f"Best pureness {max_sum} after {cycle} rotations"


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)

test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)

test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
