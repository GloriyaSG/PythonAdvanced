def path(line, position_alice):
    row, col = position_alice
    if line == "down":
        row = directions["down"][0] + row
        col = directions["down"][1] + col
    elif line == "up":
        row = directions["up"][0] + row
        col = directions["up"][1] + col
    elif line == "right":
        row = directions["right"][0] + row
        col = directions["right"][1] + col
    elif line == "left":
        row = directions["left"][0] + row
        col = directions["left"][1] + col

    return row, col


def valid_index(r, c):
    return 0 <= r < matrix_size and 0 <= c < matrix_size


matrix_size = int(input())
matrix = [input().split() for _ in range(matrix_size)]

directions = {
    "down": (1,0),
    "up": (-1,0),
    "right": (0,1),
    "left": (0,-1),
}

position_Alice = []
collected_bags = 0

for row in range(matrix_size):
    for col in range(matrix_size):
        if matrix[row][col] == "A":
            position_Alice = [row, col]
            matrix[row][col] = "*"
            break

not_valid = False

while True:
    command = input()
    row, col = path(command,position_Alice)
    if matrix[row][col] == "R" or not valid_index(row, col):
        position_Alice = [row,col]
        matrix[row][col] = "*"
        not_valid = True
        break
    elif matrix[row][col] == ".":
        position_Alice = [row, col]
        matrix[row][col] = "*"
    elif matrix[row][col].isdigit():
        collected_bags += int(matrix[row][col])
        position_Alice = [row, col]
        matrix[row][col] = "*"
    else:
        position_Alice = [row, col]

    if collected_bags >= 10:
        print("She did it! She went to the party.")
        break

if collected_bags < 10 or not_valid:
    print("Alice didn't make it to the tea party.")

print(*[' '.join(row) for row in matrix], sep="\n")
