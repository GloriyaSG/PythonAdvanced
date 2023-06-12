def concatenate(*args,**kwargs):
    word = ''.join(args)
    for key, value in kwargs.items():
        if key in word:
            word = word.replace(key,value)
    return word


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))