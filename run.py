import random


keywords = ["computer", "python", "code", "institute", "hangman", "technology",
            "algorithm", "function", "variable"]
user_gueses_list = []


def welcome_message():
    """
    Provides welcome messages and asks user if they want instructions
    on how to play
    """
    print("Welcome to Hangman...\n")
    print("Enter i for instructions...")
    instructions = str(input("Or enter any key to play!"))

    if instructions.lower() == "i":
        print("You selected instructions...\n")
        print("Guess the word using only characters a-z")
        print("Guess the word before loses all lives!\n")
        print("Good luck!")
    elif instructions != "i":
        print("Getting the game ready for you now...\n")


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
            user_gueses_list.append(user_guess)
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
        elif values in user_gueses_list:
            raise ValueError(
                print(f"You have already guessed {values} try another letter!")
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


def print_man(lives_left):
    """
    Tells user how many lives they have left whilst also printing
     hangman stages"
    """

    if lives_left == 6:
        print("   ______")
        print("  |      |")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
    elif lives_left == 5:
        print("   ______")
        print("  |      |")
        print("  |      O")
        print("  |")
        print("  |")
        print("  |")
    elif lives_left == 4:
        print("   ______")
        print("  |      |")
        print("  |      O")
        print("  |      |")
        print("  |")
        print("  |")
    elif lives_left == 3:
        print("   ______")
        print("  |      |")
        print("  |      O")
        print("  |     /|")
        print("  |")
        print("  |")
    elif lives_left == 2:
        print("   ______")
        print("  |      |")
        print("  |      O")
        print("  |     /|\ ")
        print("  |")
        print("  |")
    elif lives_left == 1:
        print("   ______")
        print("  |      |")
        print("  |      O")
        print("  |     /|\ ")
        print("  |     /")
        print("  |")
    elif lives_left == 0:
        print("   ______")
        print("  |      |")
        print("  |      O")
        print("  |     /|\ ")
        print("  |     / \ ")
        print("  |")


def validate_round():
    """
    Runs the game, sets the random word and num of lives,
    iterates through random word to create either a "_"
    or the correctly guesses letter. Takes away lives for
    incorrect guesses and ends the game if lives == 0
    """
    selected_word = random_word()
    num_of_lives = 6

    print("\n")

    correct_characters = ""
    incorrect_guess_list = []

    while num_of_lives > 0:

        outcome = ""

        for character in selected_word:
            if correct_characters.find(character) != -1:
                outcome += character
            else:
                outcome += "_"

        print(f"{outcome}\n")

        guess = get_user_guess()

        result = selected_word.find(guess)

        if result != -1:
            correct_characters += guess
            print(f"Correct! {guess} is a part of the word!\n")
        else:
            num_of_lives -= 1
            print(f"incorrect! Num of lives left {num_of_lives}")
            print_man(num_of_lives)
            incorrect_guess_list.append(guess)
            print(f"Incorrect Guesses: {incorrect_guess_list}")

        correct_word(correct_characters, selected_word)

    if num_of_lives == 0:
        print("Unlucky you have ran out of guesses!\n")
        restart_game()


def correct_word(correct_characters, selected_word):
    """
    Compares users guesses to the random selected word
    """
    is_equal = True

    for letter in selected_word:
        if letter not in correct_characters:
            is_equal = False

    if is_equal:
        print("Congratulations you win!!\n")
        restart_game()


def restart_game():
    """
    Asks user to input if they would like to restart the game or not
    """
    print("Would you like to restart the game? \n")
    restart = input("Press y to restart or any key to exit...\n")

    if restart.lower() == "y":
        print("You chose to restart!")
        print("Good Luck! \n")
        user_gueses_list.clear()
        run_round()
    elif restart != "y":
        print("You chose to exit!")
        print("Now Exiting.... \n")
        exit()


def run_round():
    """
    Run all program functions
    """
    validate_round()


welcome_message()


run_round()
