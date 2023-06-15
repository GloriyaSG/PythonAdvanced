from collections import deque


def list_manipulator(*line):
    list_num = deque(line[0])
    command = line[1]
    position = line[2]
    if len(line) == 3:
        if command == "remove":
            if position == "beginning":
                list_num.popleft()
            else:
                list_num.pop()
    elif len(line) >= 4:
        if command == "remove":
            numbers = line[-1]
            if position == "beginning":
                for amount in range(numbers):
                    list_num.popleft()
            else:
                for amount in range(numbers):
                    list_num.pop()
        elif command == "add":
            numbers = line[3:]
            if position == "beginning"  :
                for x in numbers[::-1]:
                    list_num.appendleft(x)

            elif position == "end":
                for x in numbers:
                    list_num.append(x)
    return list(list_num)



print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))

