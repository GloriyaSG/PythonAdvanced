odd = set()
even = set()

for x in range(1, int(input()) + 1):
    askii = sum(ord(char) for char in input()) // x
    if askii % 2 == 0:
        even.add(askii)
    else:
        odd.add(askii)

if sum(odd) == sum(even):
    print(*odd.union(even), sep=", ")
elif sum(odd) > sum(even):
    print(*odd.difference(even), sep=", ")
else:
    print(*odd.symmetric_difference(even), sep=", ")
