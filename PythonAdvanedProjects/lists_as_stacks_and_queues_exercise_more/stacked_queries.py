from collections import deque

stack = deque()
integer = int(input())

for x in range(integer):
    query = input()
    if "1" in query:
        query = query.split()
        num = int(query[1])
        stack.append(num)
    elif "2" in query:
        if len(stack) > 0:
            stack.pop()
    elif "3" in query:
        if len(stack) > 0:
            print(max(stack))
    else:
        if len(stack) > 0:
            print(min(stack))

stack.reverse()
print(*stack, sep=", ")