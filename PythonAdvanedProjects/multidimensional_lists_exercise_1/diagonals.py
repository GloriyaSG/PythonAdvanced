rows_cols = int(input())

matrix = [[int(x) for x in input().split(", ")] for r in range(rows_cols)]
primary = [matrix[x][x] for x in range(rows_cols)]
sec = [matrix[x][rows_cols - x - 1] for x in range(rows_cols)]

print(f"Primary diagonal: {', '.join([str(x) for x in primary])}. Sum: {sum([int(x) for x in primary])}")
print(f"Secondary diagonal: {', '.join([str(x) for x in sec])}. Sum: {sum([int(x) for x in sec])}")

