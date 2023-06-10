matrix = []
matrix_len = int(input())
for row in range(matrix_len):
    line = input()
    matrix.append(list(line))

symbol = input()
found = False
position = []
for row in range(matrix_len):
    for col in range(matrix_len):
        if matrix[row][col] == symbol:
            print(f"({row}, {col})")
            found = True
    if found:
        break
if not found:
    print(f"{symbol} does not occur in the matrix")