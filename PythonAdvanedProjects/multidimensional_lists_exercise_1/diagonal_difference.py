rows = int(input())

matrix = [[int(x) for x in input().split()] for r in range(rows)]
primary = [matrix[x][x] for x in range(rows)]
secondary = [matrix[x][rows - x - 1] for x in range(rows)]
sum_diagonals = (sum([x for x in primary])) - sum(x for x in secondary)
print(abs(sum_diagonals))