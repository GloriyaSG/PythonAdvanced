matrix = []

for row in range(int(input())):
    line = [int(x) for x in input().split(", ")]
    matrix.append(line)

print([num for sub in matrix for num in sub])