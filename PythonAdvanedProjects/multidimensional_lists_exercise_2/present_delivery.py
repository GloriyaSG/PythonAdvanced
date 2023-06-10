def cookie(position_s, childs, gifts):
    for look in santa_directions.values():
        row = position_s[0] + look[0]
        col = position_s[1] + look[1]
        if matrix[row][col] == "V":
            childs -= 1
            gifts -= 1
            matrix[row][col] = "-"
        if matrix[row][col] == "X":
            gifts -= 1
            matrix[row][col] = "-"
        if gifts == 0:
            break

    return childs, gifts

presents = int(input())
size_matrix = int(input())
matrix = [input().split() for _ in range(size_matrix)]

position_santa = []
kids = 0
kids_for_gifts = 0

santa_directions = {
    "down": (1, 0),
    "up": (-1, 0),
    "right": (0, 1),
    "left": (0, -1),
}

for row in range(size_matrix):
    for col in range(size_matrix):
        if matrix[row][col] == "S":
            matrix[row][col] = "-"
            position_santa = [row, col]
        elif matrix[row][col] == "V":
            kids_for_gifts += 1
            kids += 1


while True:
    command = input()
    if command == "Christmas morning":
        break
    row = position_santa[0] + santa_directions[command][0]
    col = position_santa[1] + santa_directions[command][1]
    position_santa = [row,col]
    if matrix[row][col] == "V":
        kids_for_gifts -= 1
        presents -= 1
        matrix[row][col] = "-"
    elif matrix[row][col] == "C":
        kids_for_gifts, presents = cookie(position_santa,kids_for_gifts,presents)
        matrix[row][col] = "S"
    elif matrix[row][col] == "X":
        matrix[row][col] = "-"
    if presents == 0:
        if kids_for_gifts != 0:
            print("Santa ran out of presents!")
            break

# matrix[position_santa[0]][position_santa[1]] = "S"

print(*[' '.join(row) for row in matrix], sep="\n")

if kids_for_gifts == 0:
    print(f"Good job, Santa! {kids} happy nice kid/s.")
else:
    print(f"No presents for {kids_for_gifts} nice kid/s.")







