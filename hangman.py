import random

# list of words for the game
words = ["python", "code", "programming", "computer", "science"]

# randomly select a word from the list
word = random.choice(words)

# variable to keep track of the number of incorrect guesses
incorrect_guesses = 0

# list to keep track of the letters that have been guessed
guessed_letters = []

# variable to keep track of whether the game is still ongoing
game_over = False

while not game_over:
    # variable to keep track of whether the player guessed the word correctly
    word_guessed = True

    # display the current state of the word (with unguessed letters replaced with _)
    for letter in word:
        if letter in guessed_letters:
            print(letter, end=' ')
        else:
            print('_', end=' ')
            word_guessed = False

    # if the player guessed the word correctly, end the game
    if word_guessed:
        print("\nCongratulations! You guessed the word.")
        game_over = True
        continue

    # get the player's guess
    guess = input("\n\nGuess a letter: ").lower()

    # check if the guess is valid (a single letter that has not been guessed before)
    if len(guess) != 1 or not guess.isalpha() or guess in guessed_letters:
        print("Invalid guess. Please enter a single letter that you haven't guessed before.")
        continue

    # add the guess to the list of guessed letters
    guessed_letters.append(guess)

    # check if the guess is in the word
    if guess in word:
        print("\nCorrect!")
    else:
        print("\nIncorrect.")
        incorrect_guesses += 1

    # if the player has made too many incorrect guesses, end the game
    if incorrect_guesses == 6:
        print("Sorry, You Lost! the word was: " + word)
        game_over = True