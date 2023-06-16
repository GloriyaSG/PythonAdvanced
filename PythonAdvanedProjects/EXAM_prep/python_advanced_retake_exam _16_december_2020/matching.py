from collections import deque

males = deque(int(x) for x in input().split())
females = deque(int(x) for x in input().split())
matches = 0

match_edits = False
while females and males:
    male = males[-1]
    if male <= 0:
        males.pop()
        continue

    if male % 25 == 0:
        males.pop()
        continue

    female = females[0]
    if female <= 0:
        females.popleft()
        continue

    if female % 25 == 0:
        females.popleft()
        continue

    if male == female:
        matches += 1
        males.pop()
        females.popleft()
    else:
        females.popleft()
        males.pop()
        males.append(male-2)


print(f"Matches: {matches}")
if males:
    males.reverse()
    print(f"Males left: {', '.join((str(x)) for x in males)}")
else:
    print("Males left: none")
if females:
    print(f"Females left: {', '.join((str(x)) for x in females)}")
else:
    print("Females left: none")



