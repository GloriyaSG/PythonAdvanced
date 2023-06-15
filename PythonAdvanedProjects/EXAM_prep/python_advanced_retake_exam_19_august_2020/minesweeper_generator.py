def near_bomb_pos(position):
    for row,col in bomb_around.values():
        row = int(row) + position[0]
        col = int(col) + position[1]
        if valid_position(row,col):
            if matrix[row][col] != "*":
                matrix[row][col] += 1

def valid_position(r, c):
    return 0 <= r < SIZE and 0 <= c < SIZE

SIZE = int(input())
bombs = int(input())
matrix = []

for _ in range(SIZE):
    line = SIZE * '0'
    matrix.append([int(x) for x in list(line)])

bomb_around = {
    "down": (1, 0),
    "up": (-1, 0),
    "right": (0, 1),
    "left": (0, -1),
    "down_left": (1,-1),
    "down_right": (1,1),
    "up_left": (-1,-1),
    "up_right": (-1,1),
}

for _ in range(bombs):
    position = [x for x in input().strip("()").split(", ")]
    row = int(position[0])
    col = int(position[1])
    matrix[row][col] = "*"

for row in range(SIZE):
    for col in range(SIZE):
        if matrix[row][col] == "*":
            pos_bomb = [row,col]
            near_bomb_pos(pos_bomb)

for row in matrix:
    print(*[', '.join(str(el)) for el in row])



