row,column = [int(x) for x in input().split(", ")]
matrix = []

for r in range(row):
    lines = [int(x) for x in input().split(", ")]
    matrix.append(lines)

sum_matrix = 0
for x in matrix:
    for y in x:
        sum_matrix += y

print(sum_matrix)
print(matrix)