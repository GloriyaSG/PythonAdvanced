def path_move(r, c, step, direction):
    new_position = []
    old_position = [r, c]
    if matrix[r][c] == ".":
        new_position = [r, c]
    else:
        return old_position
    while step != 0:
        r = r + directions[direction][0]
        c = c + directions[direction][1]
        step -= 1
        if valid_position(r, c):
            new_position = path_move(r, c, step, direction)
    return new_position


def path_shoot(r, c, dir):
    if valid_position(r, c):
        if matrix[r][c] != "x":
            if dir == "right":
                c += 1
            elif dir == "left":
                c -= 1
            elif dir == "up":
                r -= 1
            else:
                r += 1
            path_shoot(r, c, dir)
        else:
            targets_positions.append([r, c])
            matrix[r][c] = "."


def valid_position(r, c):
    return 0 <= r < 5 and 0 <= c < 5


matrix = [input().split() for _ in range(5)]

directions = {
    "down": (1, 0),
    "up": (-1, 0),
    "right": (0, 1),
    "left": (0, -1),
}

position_A = []
total_targets = 0
targets_positions = []

for row in range(5):
    for col in range(5):
        if matrix[row][col] == "A":
            position_A = [row, col]
        if matrix[row][col] == "x":
            total_targets += 1

for _ in range(int(input())):
    command = input().split()
    direction = command[1]
    if command[0] == "move":
        steps = int(command[2])
        row = position_A[0] + directions[direction][0]
        col = position_A[1] + directions[direction][1]
        if valid_position(row, col):
            position_A = path_move(row, col, steps, direction)

    elif command[0] == "shoot":
        row, col = position_A
        path_shoot(row, col, direction)

if total_targets == len(targets_positions):
    print(f"Training completed! All {total_targets} targets hit.")
else:
    print(f"Training not completed! {total_targets - len(targets_positions)} targets left.")

print(*targets_positions, sep="\n")
