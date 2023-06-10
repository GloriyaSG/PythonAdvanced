# 10 -5 20 15 -30 10
# 40 60 10 4 10 0
from collections import deque

materials = deque(int(x) for x in input().split())
magic_values = deque(int(x) for x in input().split())
magic_needed = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle",
}
crafted_toys = []
while True:
    if len(materials) == 0 or len(magic_values) == 0:
        break
    box = materials.pop()
    magic = magic_values.popleft()
    total_magic_level = box * magic
    if magic_needed.get(total_magic_level):
        crafted_toys.append(magic_needed[total_magic_level])
    elif total_magic_level < 0:
        materials.append(box + magic)
    elif magic == 0 and box == 0:
        continue
    elif box == 0:
        magic_values.appendleft(magic)
    elif magic == 0:
        materials.append(box)
    elif total_magic_level not in magic_needed:
        materials.append(box + 15)

if {"Doll", "Wooden train"}.issubset(crafted_toys) or {"Teddy bear", "Bicycle"}.issubset(crafted_toys):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join([str(x) for x in materials][::-1])}")
if magic_values:
    print(f"Magic left: {', '.join([str(x) for x in magic_values])}")

[print(f"{toy}: {crafted_toys.count(toy)}") for toy in sorted(set(crafted_toys))]
