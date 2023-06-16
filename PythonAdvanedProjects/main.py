from collections import deque

male = deque(int(x) for x in input().split())
female = deque(int(x) for x in input().split())

match = 0
while male and female:

    current_male = male[-1]
    if current_male <= 0:
        male.pop()
        continue

    if current_male % 25 == 0:
        male.pop()
        continue

    current_female = female[0]
    if current_female <= 0:
        female.popleft()
        continue

    if current_female % 25 == 0:
        female.popleft()
        continue

    if current_male == current_female:
        match += 1
        male.pop()
        female.popleft()
    else:
        female.popleft()
        current_male -= 2
        male.pop()
        male.append(current_male)

print(f"Matches: {match}")
if male:
    male.reverse()
    print(f"Males left: {', '.join([str(x) for x in male])}")
else:
    print(f"Males left: none")
if female:
    print(f"Females left: {', '.join(str(x) for x in female)}")
else:
    print(f"Females left: none")
