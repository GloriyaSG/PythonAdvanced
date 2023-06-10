matrix = input().split("|")
matrix.reverse()
new_matrix = []

for row in matrix:
    new_matrix.extend(row.split())

print(*new_matrix)