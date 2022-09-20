keywords = ["computer", "python", "code", "institute"]


def get_user_guess():
    """
    Asks user to guess a letter. Run a while loop to collect a valid input,
    which must be a letter between a-z
    """
    while True:
        print("Please enter the letter you would like to guess!")
        print("It must be between a-z and lowercase\n")

        user_guess = input(str("Enter your letter here:\n"))

        if validate_guess(user_guess):
            print("Guess is valid!")
            break
    
    return user_guess



get_user_guess()