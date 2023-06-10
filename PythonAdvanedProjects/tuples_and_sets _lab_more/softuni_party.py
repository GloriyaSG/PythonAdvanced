guests = set()

for x in range(int(input())):
    guests.add(input())

while True:
    command = input()
    if command == "END":
        break
    guests.remove(command)

print(len(guests))
for x in sorted(guests):
    print(x)