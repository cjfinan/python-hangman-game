# Hangman
My Hangman is a python terminal based game, which runs through a mock terminal on Heroku 

The user tries to guess the randomly selected word before they run out of guesses.

[You can play the game live here!](LINK HERE)


## How to play

In my version of Hangman a random word is generated, the user has to guess one letter at a time
and if the letter is within the word it will then show up however, if they get it wrong
the program will then display how many lives you have left aswell as a visual representation.

Win the game by guessing the correct word before you lose all your lives.


## Features

- Welcome message
- User can clarify any rules if they are unsure
- Or user can go straight into playing the game

![Welcome message](./images/welcome_message.png)

- Random word generated for each game

![Random word](./images/random_word.png)

- Accepts user input
- Valids user input:
  - You cannot guess more than letter at a time
  - You cannot guess anything other than a letter between a-z
  - You cannot guess a letter that you have already guessed
