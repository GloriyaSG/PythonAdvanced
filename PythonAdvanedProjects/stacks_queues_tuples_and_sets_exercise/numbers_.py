seq_1 = {int(x) for x in input().split()}
seq_2 = {int(x) for x in input().split()}

for n in range(int(input())):
    command, line, *data = input().split()
    data = [int(x) for x in data]
    if command == "Add":
        data = [int(x) for x in data]
        if line == "First":
            [seq_1.add(y) for y in data]
        else:
            [seq_2.add(y) for y in data]
    elif command == "Remove":
        if line == "First":
            [seq_1.discard(y) for y in data]
        else:
            [seq_2.discard(y) for y in data]
    else:
        print(seq_2.issubset(seq_1) or seq_1.issubset(seq_2))

print(*sorted(seq_1), sep=", ")
print(*sorted(seq_2), sep=", ")
