from collections import deque

water = int(input())

queue = deque()
command = input()

while command != "Start":
    queue.append(command)
    command = input()

while True:
    command = input()
    if command == "End":
        print(f"{water} liters left")
        break
    if "refill" in command:
        command = command.split()
        liters = int(command[1])
        water += liters
    else:
        liters = int(command)
        if water >= liters:
            print(f"{queue.popleft()} got water")
            water -= liters
        else:
            print(f"{queue.popleft()} must wait")



