def snake_move(snake, line, food, bool = False):
    row = snake[0] + move_dir[line][0]
    col = snake[1] + move_dir[line][1]
    if valid_position(row,col):
        if matrix[row][col] == "*":
            food += 1
            matrix[snake[0]][snake[1]] = "."
            snake = [row,col]
            matrix[row][col] = "S"
        elif matrix[row][col] == "B":
            pos_burrow.remove([row,col])
            matrix[row][col] = "."
            matrix[snake[0]][snake[1]] = "."
            snake = pos_burrow.pop()
            matrix[snake[0]][snake[1]] = "S"

        else:
            matrix[snake[0]][snake[1]] = "."
            snake = [row, col]
            matrix[row][col] = "S"
    else:
        matrix[snake[0]][snake[1]] = "."
        bool = True
        return snake, food, bool
    return snake, food, bool





def valid_position(r, c):
    return 0 <= r < SIZE and 0 <= c < SIZE

SIZE = int(input())

matrix = []
for row in range(SIZE):
    matrix.append([x for x in input()])
pos_snake = []
pos_burrow = []
counter = 0
for row in range(SIZE):
    for col in range(SIZE):
        if matrix[row][col] == "S":
            pos_snake = [row, col]
        if matrix[row][col] == "B":
            counter += 1
            pos_burrow.append([row,col])
move_dir = {
    "down": (1, 0),
    "up": (-1, 0),
    "right": (0, 1),
    "left": (0, -1),
}

food_counter = 0
out_bool = False
while food_counter != 10:
    command = input()
    if valid_position(pos_snake[0],pos_snake[1]):
        pos_snake, food_counter, out_bool = snake_move(pos_snake,command,food_counter, out_bool)
        if out_bool:
            print("Game over!")
            break
    else:
        print("Game over!")
        break
if food_counter >= 10:
    print("You won! You fed the snake.")

print(f"Food eaten: {food_counter}")

print(*[''.join(row) for row in matrix], sep="\n")