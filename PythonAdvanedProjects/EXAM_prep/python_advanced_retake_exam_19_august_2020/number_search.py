def numbers_searching(*numbers):
    nums = [*numbers]
    smallest = min(numbers)
    biggest = max(numbers)
    missing = []
    duplicate = []

    for num in range(smallest,biggest+1):
        if num not in numbers:
            missing.append(num)
    for el in nums:
        if nums.count(el) > 1:
            if el not in duplicate:
                duplicate.append(el)
    missing.append(sorted(duplicate))
    return missing



print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))