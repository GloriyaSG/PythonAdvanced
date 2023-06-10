unique_el = set()
for x in range(int(input())):
    command = input().split()
    for y in command:
        unique_el.add(y)
print(*unique_el, sep="\n")