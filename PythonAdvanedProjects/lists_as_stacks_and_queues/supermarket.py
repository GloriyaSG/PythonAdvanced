from collections import deque

queue = deque()

while True:
    command = input()
    if command == "End":
        print(f"{len(queue)} people remaining.")
        break
    elif command == "Paid":
        if len(queue) > 0:
            while queue:
                print(queue.popleft())
        else:
            continue
    else:
        queue.append(command)