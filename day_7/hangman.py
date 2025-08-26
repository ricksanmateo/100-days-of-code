import random

from hangman_art import stages
from hangman_words import word_list
from hangman_logo import logo

lives = 6

word = random.choice(word_list)

# print(word)

print(logo)

# display blank on length of word
placeholder = ""
for position in range(len(word)):
    placeholder += ("_")
print(placeholder)

game_over = False
correct_letters = []

while not game_over:
    # user guess
    print(f"********. You have {lives} lives remaining.********")
    guess = input("Guess a letter: ").lower()
    # print(guess)

    if guess in correct_letters:
        print(f"You already guessed {guess}")

    # check guess
    display = ""
    for letter in word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if guess not in word:
        lives -= 1

        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        if lives == 0:
            game_over = True
            print("You lose.")
            print(f"The word was {word}")

    if "_" not in display:
        game_over = True
        print("You win!")

    print(stages[lives])