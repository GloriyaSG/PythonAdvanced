intersection = set()
for _ in range(int(input())):
    first, second = [x.split(",") for x in input().split("-")]
    first_ = set(range(int(first[0]),int(first[1]) + 1))
    second_ = set(range(int(second[0]),int(second[1]) + 1))
    inter = first_.intersection(second_)
    if len(inter) > len(intersection):
        intersection = inter

print(f"Longest intersection is [{', '.join(str(x) for x in intersection)}] with length {len(intersection)}")