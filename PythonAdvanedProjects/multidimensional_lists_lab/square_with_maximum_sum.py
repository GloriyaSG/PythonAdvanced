rows,cols = [int(x) for x in input().split(", ")]

matrix = []

for x in range(rows):
    line = [int(x) for x in input().split(", ")]
    matrix.append(line)


max_sum = float('-inf')
max_sum_first_index = []
max_sum_sec_index = []
for row in range(rows-1):
    for col in range(cols-1):
        sum_matrix = matrix[row][col] + matrix[row+1][col] + matrix[row][col+1] + matrix[row+1][col+1]
        if sum_matrix > max_sum:
            max_sum = sum_matrix
            max_sum_first_index = matrix[row][col], matrix[row][col+1]
            max_sum_sec_index = matrix[row+1][col], matrix[row+1][col+1]
print(*max_sum_first_index)
print(*max_sum_sec_index)
print(max_sum)


