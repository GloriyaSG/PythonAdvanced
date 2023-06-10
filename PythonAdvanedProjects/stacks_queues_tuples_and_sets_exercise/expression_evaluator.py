from collections import deque
from functools import reduce

def reducing(operand, nums):
    result = 0
    if operand == "*":
        result = reduce(lambda x, y: x * y, nums)
    elif operand == "+":
        result = reduce(lambda x, y: x + y, nums)
    elif operand == "/":
        result = reduce(lambda x, y: x // y, nums)
    elif operand == "-":
        result = reduce(lambda x, y: x - y, nums)
    return result

string = input().split()
numbers = deque()
operators = "/*+-"
while string:
    token = string.pop(0)
    if token not in operators:
        numbers.append(int(token))
    else:
        result = reducing(token, numbers)
        numbers = deque([result])

print(numbers[0])
