import random


keywords = ["computer", "python", "code", "institute"]


def get_user_guess():
    """
    Asks user to guess a letter. Run a while loop to collect a valid input,
    which must be a letter between a-z
    """
    while True:
        print("Please enter the letter you would like to guess!")
        print("It must be between a-z\n")

        user_guess = str(input("Enter your letter here:\n"))

        if validate_guess(user_guess):
            print("Guess is valid!")
            break

    return user_guess.lower()


def validate_guess(values):
    """
    Validates users guess to see if it is one character long,
    and is aplphabetical. Returns True if criteria is met.
    """
    try:
        if len(values) != 1:
            raise ValueError(
                print("Only one letter can be guessed at any time")
            )
        elif values.isalpha() is False:
            raise ValueError(
                print("Input can only contain letters between a-z")
            )
    except ValueError:
        print(f"Incorrect data: {ValueError}\n")
        return False

    return True


def random_word():
    """
    Randomly select a word from the keywords list
    """
    selected_word = random.choice(keywords)
    return selected_word


def run_round():
    """
    Run all program functions
    """
    random_word()
    get_user_guess()


run_round()
