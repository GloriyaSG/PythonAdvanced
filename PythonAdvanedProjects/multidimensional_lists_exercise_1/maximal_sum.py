rows,cols = [int(x) for x in input().split()]

matrix = [[int(x) for x in input().split()]for x in range(rows)]

max_sum = float('-inf')

max_first = []
max_sec = []
max_third = []

for row in range(rows-2):
    for col in range(cols-2):
        sum_first = matrix[row][col] + matrix[row][col+1] + matrix[row][col+2]
        sum_sec = matrix[row+1][col] + matrix[row+1][col+1] + matrix[row+1][col+2]
        sum_third = matrix[row+2][col] + matrix[row+2][col+1] + matrix[row+2][col+2]
        if (sum_first + sum_sec + sum_third) > max_sum:
            max_sum = (sum_first + sum_sec + sum_third)
            max_first = matrix[row][col],matrix[row][col+1],matrix[row][col+2]
            max_sec = matrix[row+1][col],matrix[row+1][col+1],matrix[row+1][col+2]
            max_third = matrix[row+2][col],matrix[row+2][col+1],matrix[row+2][col+2]
print(f"Sum = {max_sum}")
print(*max_first)
print(*max_sec)
print(*max_third)
