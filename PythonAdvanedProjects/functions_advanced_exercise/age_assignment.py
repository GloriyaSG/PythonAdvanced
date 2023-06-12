def age_assignment(*args,**kwargs):
    result = []
    for key,value in kwargs.items():
        for name in args:
            if name.startswith(key):
                result.append(f"{name} is {value} years old.")
    return '\n'.join(sorted(result, key=lambda x: x[0]))



print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))