from art import logo
import helper
import random
import signal
from os import system


def handler(signum, frame):
    system("cls")
    exit(1)


signal.signal(signal.SIGINT, handler)


def start_game():
    print("Welcome to the Number Guessing Game!")
    play_again = True
    while play_again:
        play_again = play_game()
    system("cls")


def play_game():
    system("cls")
    print(logo)
    limit = helper.validate_user_input_number(input("Until which number would you like to guess: "))
    number_to_guess = random.randint(1, limit)
    difficulty = helper.validate_user_input_level(input("Choose a difficulty. Type 'easy' or 'hard': "))
    attempts = 10
    if difficulty != "easy": attempts = 5
    print(f"You have {attempts} attempts remaining to guess the number.")
    user_guess = helper.validate_user_input_limit(input("Make a guess: "), limit)
    guess_range = limit / 10
    win = False
    for i in reversed(range(1, attempts)):
        win = check_user_guess(user_guess, number_to_guess, guess_range)
        if win:
            print(f"You got it! The answer is {user_guess}")
            break
        if not win:
            print(f"You have {i} attempts remaining to guess the number.")
            user_guess = helper.validate_user_input_limit(input("Guess again: "), limit)
    if not win: print("You run out of guesses, you lose")
    return helper.validate_user_input_play_again(input("Do you want to play again? (y/n) ")) == 'y'


def check_user_guess(user_guess, number_to_guess, guess_range):
    if user_guess == number_to_guess: return True
    if user_guess < number_to_guess: helper.handle_low_guess(user_guess, number_to_guess, guess_range)
    else: helper.handle_high_guess(user_guess, number_to_guess, guess_range)
    return False


start_game()
