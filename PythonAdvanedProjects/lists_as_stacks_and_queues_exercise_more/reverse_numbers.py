from collections import deque

nums = deque([int(x) for x in input().split()])

nums.reverse()
print(*nums)