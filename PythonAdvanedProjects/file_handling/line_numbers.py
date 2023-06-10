from string import punctuation
new_file = open("output.txt",'w')

with open("text.txt", 'r') as file:
    lines = file.readlines()

    for index in range(0, len(lines)):
        line = ''.join(lines[index].split("\n"))
        counter_alpha = 0
        counter_symbols = 0

        for char in line:
            if char == "\\":
               continue
            if char == " ":
                continue
            if char in punctuation:
                counter_symbols +=1
            else:
                counter_alpha += 1

        new_file.write(f"Line {index+1}: {line} ({counter_alpha})({counter_symbols})\n")
        new_file.close()