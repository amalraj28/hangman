import random
from hangman_words import word_list
from hangman_art import *
from termcolor import colored

random_word = random.choice(word_list)  # Select random word from available list of words
blank_list = list()
for _ in random_word:
    blank_list.append('_')
    # This is to create a string having as many underscores as the number of letters of random word
    # This list will be converted to string as and when required using join method

print(logo)
print(f"\nGuess the word: {' '.join(blank_list)}")
lives = 6

while lives:

    # If the correct letter is entered, that will be filled in the blanks
    # If the wrong letter is entered, one life will be reduced and the corresponding hangman image is shown

    letter = input('\nEnter a letter: ').lower()
    if letter not in random_word:
        lives -= 1
        print(stages[lives])
        print(' '.join(blank_list))
        continue

    print(stages[lives])
    for pos in range(len(random_word)):     # This is to replace each blank with the correct letter
        if random_word[pos] == letter:
            blank_list[pos] = letter.upper()

    print(' '.join(blank_list))

    if '_' not in blank_list:

        # If _ is not there, it implies that the correct word has been guessed

        print(f"\nYeeee!!! You guessed the word {colored(random_word.upper(), 'red', on_color='on_white', attrs=['bold', 'underline'])} correctly!")
        break

    else:
        continue

if not lives:

    # If lives = 0, implies the user has exhausted his chances. Then the correct word is printed

    print(f'\nWord is', end=' ')
    print(colored(random_word.upper(), 'red', on_color='on_white', attrs=['bold', 'underline']))  # To print the word in Red colour with White background
    print()
