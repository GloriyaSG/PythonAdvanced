# 1 + (2 - (2 + 3) * 4 / (3 + 1)) * 5

# (2 + 3)
# (3 + 1)
# (2 - (2 + 3) * 4 / (3 + 1))

from collections import deque

text = input()
parentheses = [] #(()

for x in range(len(text)):
    if text[x] == "(":
        parentheses.append(x)
    if text[x] == ")":
        index_start = parentheses.pop()
        print(text[index_start:x + 1])
