def valid_index(r,c):
    if 0 <= r <= rows - 1 and 0 <= c <= rows - 1:
        return True
    else:
        print("Invalid coordinates")


rows = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(rows)]

while True:
    command = input().split()
    if command[0] == "END":
        for rows in matrix:
            print(*rows,sep=" ")
        break

    row, col, value = int(command[1]), int(command[2]), int(command[3])
    if valid_index(row,col):

        if command[0] == "Add":
            matrix[row][col] += value

        elif command[0] == "Subtract":
            matrix[row][col] -= value


