from collections import deque

clothes_in_box = deque([int(x) for x in input().split()])

capacity_one_rack = int(input())

total_racks = 1
capacity = capacity_one_rack

while clothes_in_box:
    cloth = clothes_in_box.pop()
    if capacity >= cloth:
        capacity -= cloth
    else:
        total_racks += 1
        capacity = capacity_one_rack - cloth

print(total_racks)
