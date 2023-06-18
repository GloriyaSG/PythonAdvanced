def mouse_moves(mouse_pos, direction, game_over,cheeses):
    row = mouse_pos[0] + directions[direction][0]
    col = mouse_pos[1] + directions[direction][1]
    if not valid_position(row,col):
        game_over = True
        print("No more cheese for tonight!")
    else:
        if matrix[row][col] == "C":
            matrix[mouse_pos[0]][mouse_pos[1]] = "*"
            cheeses -= 1
            mouse_pos = [row, col]
            matrix[row][col] = "M"
            if cheeses == 0:
                print("Happy mouse! All the cheese is eaten, good night!")
                game_over = True
        elif matrix[row][col] == "T":
            matrix[mouse_pos[0]][mouse_pos[1]] = "*"
            matrix[row][col] = "M"
            print("Mouse is trapped!")
            game_over = True
        elif matrix[row][col] == "*":
            matrix[mouse_pos[0]][mouse_pos[1]] = "*"
            mouse_pos = [row, col]
            matrix[row][col] = "M"

    return mouse_pos, game_over, cheeses


def valid_position(r, c):
    return 0 <= r < rows and 0 <= c < cols


rows, cols = [int(x) for x in input().split(",")]
matrix = []
mouse = []
cheese = 0

for row in range(rows):
    col = [''.join(x) for x in input()]
    matrix.append(col)

for row in range(rows):
    for col in range(cols):
        if matrix[row][col] == "M":
            mouse = [row,col]
        elif matrix[row][col] == "C":
            cheese += 1

directions = {
    "down": (1,0),
    "up": (-1,0),
    "right": (0,1),
    "left": (0,-1),
}
game_over_mouse = False

while True:
    command = input()
    if command == "danger":
        if cheese != 0:
            print("Mouse will come back later!")
        break
    mouse, game_over_mouse, cheese = mouse_moves(mouse,command,game_over_mouse, cheese)
    if game_over_mouse:
        break
for row in matrix:
    print(*row, sep="")