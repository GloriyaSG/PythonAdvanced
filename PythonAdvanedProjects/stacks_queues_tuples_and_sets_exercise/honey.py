from collections import deque


def operate(operator, worker, nect):
    result = 0
    if operator == "*":
        result = worker * nect
    elif operator == "/":
        result = worker / nect
    elif operator == "+":
        result = worker + nect
    else:
        result = worker - nect
    return abs(result)


bees = deque(int(x) for x in input().split())
nectars = deque(int(x) for x in input().split())
symbols = deque(x for x in input().split())
honey_made = 0
while True:
    if len(bees) == 0 or len(nectars) == 0:
        break
    bee = bees.popleft()
    nectar = nectars.pop()
    if nectar > bee:
        symbol = symbols.popleft()
        honey_made += operate(symbol,bee,nectar)
    elif nectar < bee:
        bees.appendleft(bee)

print(f"Total honey made: {honey_made}")
if bees:
    print(f"Bees left: {', '.join(str(x) for x in bees)}" )
if nectars:
    print(f"Nectar left: {', '.join(str(x) for x in nectars)}" )
