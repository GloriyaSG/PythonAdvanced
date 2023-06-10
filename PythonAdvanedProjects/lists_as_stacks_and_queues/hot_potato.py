from collections import deque

kids_name = deque(input().split())
toss = int(input()) - 1

while True:
    if len(kids_name) == 1:
        print(f"Last is {''.join(kids_name)}")
        break
    kids_name.rotate(-toss)
    name = kids_name.popleft()
    print(f"Removed {name}")

