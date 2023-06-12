def stronger(positives,negatives):

    print(negatives)
    print(positives)

    if abs(negatives) > positives:
        print("The negatives are stronger than the positives")

    else:
        print("The positives are stronger than the negatives")


numbers = [int(x) for x in input().split()]
positive = sum(num for num in numbers if num > 0)
negative = sum(num for num in numbers if num < 0)
stronger(positive,negative)


