nums = [1,2,2,3,4,4,5,6]
dublicates = []
for el in nums:
    if nums.count(el) > 1:
        if el not in dublicates:
            dublicates.append(el)
print(dublicates)