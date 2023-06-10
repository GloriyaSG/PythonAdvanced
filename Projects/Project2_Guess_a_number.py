import random
pc_number = random.randint(1, 100)
while True:
    player_input = input("Guess a number from 1 to 100:")

    if not player_input.isdigit():
        print("Invalid!Try ")