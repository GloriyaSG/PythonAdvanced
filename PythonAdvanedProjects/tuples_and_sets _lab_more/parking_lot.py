record = set()

for x in range(int(input())):
    data = input().split(", ")
    if data[0] == "IN":
        record.add(data[1])
    else:
        record.remove(data[1])

if record:
    cars = [x for x in record]
    print(*cars,sep="\n")
else:
    print("Parking Lot is Empty")

