rows, cols = [int(x) for x in input().split()]

alpha = ord("a")
for row in range(alpha, alpha + rows):
    for col in range(row, row + cols):
        print(f"{chr(row)}{chr(col)}{chr(row)}", end=" ")
    print()