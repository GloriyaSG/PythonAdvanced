nums = tuple([float(x) for x in input().split()])
counter = {}
for x in nums:
    if x not in counter:
        counter[x] = nums.count(x)

[print(f"{key} - {counter[key]} times") for key in counter]