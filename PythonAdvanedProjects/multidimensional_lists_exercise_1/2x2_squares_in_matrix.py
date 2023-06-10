rows, cols = [int(x) for x in input().split()]
matrix = []

for r in range(rows):
    line = input().split()
    matrix.append(line)
squares = 0
for row in range(rows - 1):
    for col in range(cols - 1):
        if matrix[row][col] == matrix[row][col+1]:
            if matrix[row][col] == matrix[row+1][col]:
                if matrix[row+1][col] == matrix[row+1][col+1]:
                    squares += 1


print(squares)