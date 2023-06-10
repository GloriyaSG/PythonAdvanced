record = {}

for x in range(int(input())):
    name, grade = input().split()
    if name not in record:
        record[name] = []
    record[name].append(float(grade))

for x in record:
    average = sum(record[x]) / len(record[x])
    grades = ' '.join([f'{g:.2f}' for g in record[x]])
    print(f"{x} -> {grades} (avg: {average:.2f})")

