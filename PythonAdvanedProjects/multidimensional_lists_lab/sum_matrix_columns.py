rows, columns = [int(x) for x in input().split(", ")]

matrix = []
for row in range(rows):
    line = [int(x) for x in input().split()]
    matrix.append(line)
sum = 0
for column in range(columns):
    total_sum = 0
    for row in range(rows):
        total_sum += matrix[row][column]
    print(total_sum)

