import random
import string
from words import words


def get_valid_word(words):
    word = random.choice(words)  # randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)
        word.upper()

    return word


def play_game():
    word = get_valid_word(words)
    word = word.upper()
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 7

    while len(word_letters) > 0 and lives > 0:
        # letters used
        print("\nYou have used the following letters: ", ' '.join(used_letters))
        print(f"Remaining lives: {lives}")

        # what current word is
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        used_letter = input("Type a character: ")
        used_letter = used_letter.upper()
        if used_letter in alphabet - used_letters:
            used_letters.add(used_letter)
            if used_letter in word_letters:
                word_letters.remove(used_letter)
                print('')
            else:
                lives -= 1
                print("Your letter is not in the word!")

        elif used_letter in used_letters:
            print("You've already used that character!")

        else:
            print("Invalid character!")

    if lives == 0:
        print(f"You died! The word was {word}")
    else:
        print(f"You guessed the word! - {word}")


if __name__ == '__main__':
    play_game()
