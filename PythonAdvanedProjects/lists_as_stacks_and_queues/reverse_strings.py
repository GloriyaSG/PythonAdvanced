string = list(input())

stack = []

for x in range(len(string)):
    stack.append(string.pop())

print("".join(stack))
