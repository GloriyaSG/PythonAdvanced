from collections import deque

stack = deque(input())
open_par = deque()

while stack:
    bracket = stack.popleft()
    if bracket in "([{":
        open_par.append(bracket)
    elif not open_par:
        print("NO")
        break
    else:
        last_open = open_par.pop()
        if last_open + bracket not in "{}()[]":
            print("NO")
            break
else:
    print("YES")


