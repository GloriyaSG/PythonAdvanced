matrix = []
sum_diagonal = 0
for row in range(int(input())):
    line = [int(x) for x in input().split()]
    matrix.append(line)
    sum_diagonal += matrix[row][row]

print(sum_diagonal)
