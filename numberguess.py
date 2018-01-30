"""This program asks a user to guess the roll of a die (or dice).  The person with the closest guess is the winner."""

from random import randint
from time import sleep


def get_user_guess(max_value):  # accepts the max a user can choose which is 2x the number of sides of a die
    user_guess = int(input("Guess the roll of the die. Type a number from 2-%d: " % max_value))
    if user_guess >= 2 and user_guess <= max_value:
        print("\nYou've guessed %d" % user_guess)
        return user_guess
    else:
        print("\nYou entered %d which is not from 2-%d. Try again." % (user_guess, max_value))
        user_guess = int(input("Guess the roll of the die. Type a number from 2-%d: " % max_value))
        if user_guess < 2 or user_guess > max_value:
            print("\nYou're obviously too stupid for this game.")
            user_guess = 1
            return user_guess
        else:
            return user_guess


def roll_dice(number_of_sides):  # simulates rolling dice after receiving the number of sides the dice have
    first_roll = randint(1, number_of_sides)
    second_roll = randint(1, number_of_sides)
    total_roll = first_roll + second_roll
    max_val = 2 * number_of_sides
    print("\nYou have two %d-sided dice and can roll anything from 2 to %d." % (number_of_sides, max_val))
    sleep(1)
    user_guess = get_user_guess(max_val)
    if user_guess == 1:
        print("\nGoodbye.")
        return
    else:
        print("\nRolling ...")
        sleep(1)
        print("\nOK. The first die says %d." % first_roll)
        sleep(1)
        print("\nThe second die says %d. Your total is %d." % (second_roll, total_roll))
        sleep(1)
        if user_guess >= total_roll:
            print("\n\nCongratulations! You're a winner. Winner, winner chicken dinner!")
            return
        else:
            print("\n\nBetter luck next time. Your roll was less than the dice.")
            return


print("We're playing dice! To win, guess equal to or higher than the 2 dice rolled.")
sides = int(input("To get started, tell us how many sides the dice have: "))
roll_dice(sides)
