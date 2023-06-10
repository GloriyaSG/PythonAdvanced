import os

while True:
    command = input().split("-")

    if command[0] == "End":
        break

    if command[0] == "Create":
        with open(f"{command[1]}", "w"): pass

    elif command[0] == "Add":
        file_name = command[1]
        content = command[2]
        with open(f"{file_name}", "a") as file:
            file.write(f"{content}\n")

    elif command[0] == "Replace":
        file_name = command[1]
        old_string = command[2]
        new_string = command[3]

        try:
            with open(f"{file_name}","r+") as file:
                txt = file.read()
                txt = txt.replace(old_string,new_string,-1)

                file.seek(0,0)
                file.write(txt)

        except FileNotFoundError:
            print(f"An error occurred")
    elif command[0] == "Delete":
        file_name = command[1]

        try:
            os.remove(f"{file_name}")
        except FileNotFoundError:
            print("An error occurred")











