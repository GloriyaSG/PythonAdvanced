symbols = ["-", ",", ".", "!", "?"]

with open("text.txt", 'r') as file:
    lines = file.readlines()

for index in range(0,len(lines),2):
    txt = lines[index]

    for char in txt:
        if char in symbols:
            txt = txt.replace(char,"@")

    print(*txt.split()[::-1])

