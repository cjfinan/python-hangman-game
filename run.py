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


def print_man(lives_left):
    """
    Tells user how many lives they have left whilst also printing
     hangman stages"
    """
    
    print(f"Current lives: {lives_left}")

    if lives_left == 8:
        print("_")
    elif lives_left == 7:
        print("__")
    elif lives_left == 6:
        print("__")
        print("  |")
    elif lives_left == 5:
        print(" __")
        print("   |")
        print("   O")
    elif lives_left == 4:
        print(" __")
        print("   |")
        print("   O")
        print("   |")
    elif lives_left == 3:
        print(" __")
        print("   |")
        print("   O")
        print("  /|")
    elif lives_left == 2:
        print(" __")
        print("   |")
        print("   O")
        print("  /|\ ")
    elif lives_left == 1:
        print(" __")
        print("   |")
        print("   O")
        print("  /|\ ")
        print("  /")
    elif lives_left == 0:
        print(" __")
        print("   |")
        print("   O")
        print("  /|\ ")
        print("  / \ ")



def validate_round():
    selected_word = random_word()
    num_of_lives = 9
    #outcome variable = ""
    #append character to variable
    #creat variable correct character list
    # move for loop into while loop
    for character in selected_word:
        if correct_characters contains (character):
            outcome varibale += character
        else
            outcome variable += "_"
       # print("_", end=' ')
    print outcome variable
    print("\n")
    print(f"random word : {selected_word}")


    
    #correct character contains an _
    while num_of_lives != 0 or outcome variable contains _:
        guess = get_user_guess()
        print(f"guess : {guess}")

        result = selected_word.find(guess)
        print(result)

        if result == -1:
            num_of_lives -= 1
            print(f"incorrect! Num of lives left {num_of_lives}")
            print_man(num_of_lives)
        else:
            correct_characters.append(guess)
            print(f"correct! correct scores: {correct_guesses}")
    


def run_round():
    """
    Run all program functions
    """

    validate_round()
    

   # result = word.find(guess)
   # print(result)


run_round()

#check if c is already guessed
#