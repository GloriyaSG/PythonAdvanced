def indices(par1,par2,par3,par4):
    if 0 <= par1 <= rows and 0 <= par2 <= cols and 0 <= par3 <= rows and 0 <= par4 <= cols:
        matrix[par1][par2], matrix[par3][par4] = matrix[par3][par4], matrix[par1][par2]
        print(*[' '.join(x) for x in matrix], sep="\n")
    else:
        print("Invalid input!")


rows, cols = [int(x) for x in input().split()]

matrix = [input().split() for x in range(rows)]

while True:
    command = input()
    if command == "END":
        break
    else:
        command, *data = command.split()
        if command == "swap":
            row1, col1, row2, col2 = [int(x) for x in data]
            indices(row1,col1,row2,col2)
        else:
            print("Invalid input!")

