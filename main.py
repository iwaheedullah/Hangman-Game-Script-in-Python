# Import random library.
import random
from hangman_words import word_list

# lives of a player.
LIVES = 6

# Flag word
is_game_finished = False

# Pick the random word.
random_word = random.choice(word_list)
random_word_length = len(random_word)

# Blank spaces.
blanks = []
for _ in range(random_word_length):
    blanks += '_'

while not is_game_finished:

    user_guess = input("Guess the word: ").lower()

    # if letter is already guessed.
    if user_guess in blanks:
        print("Letter is already Guessed. Try Another one. ")

    # Find position and place it there, if guessed correctly.
    for position in range(random_word_length):
        letter = random_word[position]

        if letter == user_guess:
            blanks[position] = user_guess

    # if guessed invalid letters.
    if user_guess not in random_word:
        LIVES -= 1
        print(f"You have guessed Invalid letter {user_guess}. Try Again. Remaining LIVES: ", LIVES)

        # decrement a lives.
        if LIVES == 0:
            is_game_finished = True
            print("You run out of lives. Game Over.")

    # print the blanks.
    print(f"{' '.join(blanks)}")

    # When the whole guessed correctly.
    if '_' not in blanks:
        is_game_finished = True
        print("\nAll the letter are guessed correctly. Won it.")
