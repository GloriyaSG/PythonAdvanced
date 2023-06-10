rock = "Rock"
paper = "Paper"
scissors = "Scissors"
player_move = input("Chose [r]ock, [p]aper or [s]cissors:")
pc_move = ""
if player_move == "r":
    player_move = rock
elif player_move == "p":
    player_move = paper
elif player_move == "s":
    player_move = scissors
else:
    raise SystemExit("Invalid! Try again...")

import random

pc_random_num = random.randint(1, 3)
if pc_random_num == 1:
    pc_move = rock
elif pc_random_num == 2:
    pc_move = paper
else:
    pc_move = scissors

print(f"The computer chose {pc_move}.")

if player_move == rock:
    if pc_move == scissors:
        print("You win!")
    elif pc_move == paper:
        print("You lose!")
    elif pc_move == rock:
        print("Draw")
elif player_move == scissors:
    if pc_move == paper:
        print("You win!")
    elif pc_move == rock:
        print("You lose!")
    elif pc_move == scissors:
        print("Draw")
elif player_move == paper:
    if pc_move == rock:
        print("You win!")
    elif pc_move == scissors:
        print("You lose!")
    elif pc_move == paper:
        print("Draw")