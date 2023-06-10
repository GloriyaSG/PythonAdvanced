def valid_index(r, c):
        if 0 <= r < size_field and 0 <= c < size_field:
            return True


size_field = int(input())
matrix = [input().split() for _ in range(size_field)]

positions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

max_eggs = 0
position_of_bunny = []
max_directions = ""
best_way = []


for row in range(size_field):
    for col in range(size_field):
        if matrix[row][col] == "B":
            position_of_bunny = [row, col]

for direction, position in positions.items():
    row = position[0] + position_of_bunny[0]
    col = position[1] + position_of_bunny[1]

    eggs = 0
    road = []

    while valid_index(row,col):
        if matrix[row][col] == "X":
            break
        eggs += int(matrix[row][col])
        road.append([row,col])
        row += position[0]
        col += position[1]

    if eggs >= max_eggs:
        max_eggs = eggs
        max_directions = direction
        best_way = road

print(max_directions)
print(*best_way,sep="\n")
print(max_eggs)
