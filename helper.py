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
    while user_input not in range(1, limit):
        user_input = input(f"Only numbers between 1 and {limit} are allowed. Try again.\n")
    return user_input


def validate_user_input_play_again(user_input):
    while user_input.lower() not in ["y", "n"]:
        user_input = input("Wrong input. Try again.\n").lower()
    return user_input
