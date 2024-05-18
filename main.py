import os
import random
from hangman_words import word_list
from hangman_art import logo, stages

# Choose a random word from the word list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(logo)

# Create blanks
display = ["_"] * word_length

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # Clear the console
    os.system('cls' if os.name == 'nt' else 'clear')

    # Check if the guess is a single letter
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    # Check if the letter has already been guessed
    if guess in display:
        print(f"You've already guessed {guess}")
    else:
        # Check guessed letter
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter

        # Check if user is wrong
        if guess not in chosen_word:
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
            lives -= 1
            if lives == 0:
                end_of_game = True
                print("You lose.")
        else:
            print(f"Good job! {guess} is in the word.")

    # Join all the elements in the list and turn it into a string
    print(f"{' '.join(display)}")

    # Check if user has guessed all letters
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])
