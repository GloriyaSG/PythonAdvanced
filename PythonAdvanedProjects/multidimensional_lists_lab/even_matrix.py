matrix = []

rows = int(input())

for row in range(rows):
    inner = [r for r in [int(x) for x in input().split(", ")] if r % 2 == 0]
    matrix.append(inner)

print(matrix)

