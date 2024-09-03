def validate_user_input_number(user_input):
    while not user_input.isdigit():
        user_input = input("Only integer numbers are allowed. Try again: ")
    return int(user_input)


def validate_user_input_level(user_input):
    while user_input.lower() not in ["easy", "hard"]:
        user_input = input("Wrong input. Try again: ").lower()
    return user_input


def validate_user_input_limit(user_input, limit):
    user_input = validate_user_input_number(user_input)
    while user_input not in range(1, limit + 1):
        user_input = input(f"Only numbers between 1 and {limit} are allowed. Try again: ")
    return user_input


def validate_user_input_play_again(user_input):
    while user_input.lower() not in ["y", "n"]:
        user_input = input("Wrong input. Try again: ").lower()
    return user_input


def handle_low_guess(user_guess, number_to_guess, guess_range):
    if user_guess < number_to_guess - (guess_range * 3):
        print("Extremely low guess.")
    elif user_guess < number_to_guess - (guess_range * 2):
        print("Too low guess.")
    else:
        print("Low guess.")


def handle_high_guess(user_guess, number_to_guess, guess_range):
    if user_guess > number_to_guess + (guess_range * 3):
        print("Extremely high guess.")
    elif user_guess > number_to_guess + (guess_range * 2):
        print("Too high guess.")
    else:
        print("High guess.")
