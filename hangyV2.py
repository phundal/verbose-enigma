#!/usr/bin/env python3

"""

Hangman

this python file will be the logic behind the visual version of the hangman game.

"""

import random


def main():
    welcome = ['Welcome to Hangman! A word will be chosen at random and',
               'you must try to guess the word correctly letter by letter',
               'before you run out of attempts. Good luck!'
               ]

    print("\n".join(welcome))

    # setting up the play_again loop

    play_again = True

    while play_again:
        # set up the game loop

        words = ["hangman", "chairs", "backpack", "bodywash", "clothing",
                 "computer", "python", "program", "glasses", "sweatshirt",
                 "sweatpants", "mattress", "friends", "clocks", "biology",
                 "algebra", "suitcase", "knives", "ninjas", "shampoo"
                 ]

        chosen_word = random.choice(words).lower()
        player_guess = None  # will hold the players guess
        guessed_letters = []  # a list of letters guessed so far
        word_guessed = []
        for letter in chosen_word:
            word_guessed.append("-")  # create an unguessed, blank version of the word
        joined_word = None  # joins the words in the list word_guessed

        # build the characters that show the hangman
        HANGMAN = (
            """
-----
|   |
|
|
|
|
|
|
|
--------
""",
            """
-----
|   |
|   0
|
|
|
|
|
|
--------
""",
            """
-----
|   |
|   0
|  -+-
|
|
|
|
|
--------
""",
            """
-----
|   |
|   0
| /-+-
|
|
|
|
|
--------
""",
            """
-----
|   |
|   0
| /-+-\\
|
|
|
|
|
--------
""",
            """
-----
|   |
|   0
| /-+-\\
|   |
|
|
|
|
--------
""",
            """
-----
|   |
|   0
| /-+-\\
|   |
|   |
|
|
|
--------
""",
            """
-----
|   |
|   0
| /-+-\\
|   |
|   |
|  |
|
|
--------
""",
            """
-----
|   |
|   0
| /-+-\
|   |
|   |
|  |
|  |
|
--------
""",
            """
-----
|   |
|   0
| /-+-\\
|   |
|   |
|  | |
|  |
|
--------
""",
            """
-----
|   |
|   0
| /-+-\\
|   |
|   |
|  | |
|  | |
|
--------
""")

        print(HANGMAN[0])
        attempts = len(HANGMAN) - 1

        while (attempts != 0 and "-" in word_guessed):

            print(("\nYou have {} attempts remaining").format(attempts))
            print("".join(word_guessed))

            print("Letters you have guessed:", ", ".join(sorted(guessed_letters)))

            player_guess = input('Please select a letter between [a-z] > ')

            # Lets check some excpetions
            if not player_guess.isalpha():  # check the input is a letter. Also checks an input has been made.
                print("That is not a letter. Please try again.")
            elif player_guess.lower() == "".join(chosen_word):  # did they guess the word early?
                word_guessed = chosen_word
            elif len(player_guess) > 1:  # check the input is only one letter
                print("That is more than one letter. Please try again.")
            elif player_guess.lower() in guessed_letters:  # check it letter hasn't been guessed already
                print("You have already guessed that letter. Please try again.")
            else:  # legitimate letter, so game on!
                guessed_letters.append(player_guess.lower())
                for letter in range(len(chosen_word)):
                    if player_guess.lower() == chosen_word[letter]:
                        # replace all letters in the chosen word that match the players guess
                        word_guessed[letter] = player_guess.lower()
                if (player_guess.lower() not in chosen_word):
                    attempts -= 1
                    print(HANGMAN[(len(HANGMAN) - 1) - attempts])

        # lets check if the word has been fully guessed by the time the guesses run out
        if "-" not in word_guessed:  # no blanks remaining
            print(f"\nCongratulations! \"{chosen_word}\" was the word!")
        else:  # loop must have ended because attempts reached 0
            print(f"\nUnlucky! The word was \"{chosen_word}\".")

        # game is over, should we play again?
        response = input("\nWould you like to play again? > ")
        if response.lower() not in ("yes", "y"):
            play_again = False


if __name__ == "__main__":
    main()
