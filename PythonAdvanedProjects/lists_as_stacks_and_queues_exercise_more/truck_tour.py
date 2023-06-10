from collections import deque
n = int(input())
stack = deque([int(y) for y in input().split()] for _ in range(n))
copy = stack.copy()
tank = 0
starter = 0

while copy:
    petrol, dist = copy.popleft()
    tank += petrol
    if tank >= dist:
        tank -= dist
    else:
        stack.rotate(n-1)
        copy = stack.copy()
        starter += 1
        tank = 0
print(starter)

# 3
# 1 5
# 10 3
# 3 4



