from collections import deque

food_per_day = int(input())
food_per_order = deque([int(x) for x in input().split()])

print(max(food_per_order))

for order in food_per_order.copy():
    if order <= food_per_day:
        food_per_order.remove(order)
        food_per_day -= order
    else:
        break

if len(food_per_order) == 0:
    print("Orders complete")
else:
    left_orders = " ".join([str(x) for x in food_per_order])
    print(f"Orders left: {left_orders}")