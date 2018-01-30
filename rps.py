"""A CodeAcademy programme to play Rock, Paper, Scissors - maybe add in a bang or something fun too"""

from random import randint
from time import sleep

options = [
    "R", "P", "S"
]

LOSS = "\nYou lost! Come again another time."
WIN = "\nWinner, Winner, Chicken Dinner"


def decide_winner(user_choice, computer_choice):
    print("You chose %s" % user_choice)
    print("\nThe big bad computer will choose next ...")
    sleep(1)
    print("\nBAM! The computer chose %s" % computer_choice)
    user_choice_index = options.index(user_choice)
    computer_choice_index = options.index(computer_choice)
    if user_choice_index == computer_choice_index:
        print("\nBoring. It's a push. Try again.")
    elif user_choice_index == 0 and computer_choice_index == 2:
        print(WIN)
    elif user_choice_index == 1 and computer_choice_index == 0:
        print(WIN)
    elif user_choice_index == 2 and computer_choice_index == 1:
        print(WIN)
    elif user_choice_index > 2:
        print("\nNo cheating. Try again.")
    else:
        print(LOSS)


def play_rps():
    print("You're about to play Rock ... Paper ... Scissors. The classic game of strategy and skill.")
    user_choice = input("Enter R, P, or S to play.")
    if user_choice[0].upper() in options:
        computer_choice = options[randint(0, len(options) - 1)]
        decide_winner(user_choice.upper(), computer_choice)
    else:
        print("You've not chosen R, P, or S so we can't play. Try again.")


play_rps()
# decide_winner("R","P")
