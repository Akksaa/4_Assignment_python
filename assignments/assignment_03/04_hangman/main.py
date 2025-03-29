import random
import string
from words import words

def get_valid_word(words):
    """Chooses a valid word from the list, avoiding words with spaces or hyphens."""
    word=random.choice(words)
    while '-' in word or ' ' in word:
        word=random.choice(words)
    return word.upper()

def hangman():
    """Runs the Hangman game logic"""
    word=get_valid_word(words)
    word_letters= set(word)
    used_letters= set()
    alphabet= set(string.ascii_uppercase)
    lives = 7
    while word_letters and lives > 0:
        print(f"\nLives left: {lives}")
        print("Used letters: ", ' '.join(sorted(used_letters)))

        word_display=[letter if letter in used_letters else '-' for letter in word]
        print("Current word: ", ' '.join(word_display))

        user_letter=input("Guess a letter: ").upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives-= 1
                print(f"Wrong guess! {user_letter} is not in the word. ")
        elif user_letter in used_letters:
            print("You already guessed that letter.Try again")
        else:
            print("Invalid input. Please enter a letter.")
    if lives==0:
        print(f"\nGame Over! The word was {word}.")
    else:
        print(f"Congratulations! You guessd the word {word}.")


def main():
    hangman()


if __name__ == "__main__":
    main()
