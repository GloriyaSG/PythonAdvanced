from collections import deque

chocolate = deque(int(x) for x in input().split(","))
cup_milks = deque(int(x) for x in input().split(","))
milkshakes = 0

while chocolate and cup_milks and milkshakes != 5:
    chocolate_piece = chocolate.pop()
    milk_piece = cup_milks.popleft()
    if chocolate_piece <= 0 and milk_piece <= 0:
        continue
    elif chocolate_piece <= 0:
        cup_milks.appendleft(milk_piece)
        continue
    elif milk_piece <= 0:
        chocolate.append(chocolate_piece)
        continue
    if chocolate_piece == milk_piece:
        milkshakes += 1
    else:
        cup_milks.append(milk_piece)
        chocolate.append(chocolate_piece - 5)

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolate:
    print(f"Chocolate: {', '.join([str(x) for x in chocolate])}")
else:
    print("Chocolate: empty")
if cup_milks:
    print(f"Milk: {', '.join([str(x) for x in cup_milks])}")
else:
    print("Milk: empty")