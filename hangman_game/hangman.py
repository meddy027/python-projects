import random
import string
from words import words


class hangman_game:
    def __init__(self, words, lives):
        self.words = words
        self.lives = lives

    def get_valid_word(self):
        word = random.choice(self.words)
        return word.upper()

    def play_hangman(self, word):
        valid_letters = set(word)
        alphabet = set(string.ascii_letters)
        used_letters = set()
        while len(valid_letters) > 0 and self.lives > 0:
            print(
                "Letters used: ",
                " ".join(used_letters),
                "\nYou have",
                self.lives,
                "left to guess the word.",
            )
            words_list = [letter if letter in used_letters else "-" for letter in word]
            print("Current word:", " ".join(words_list))
            user_input = input("Enter a letter: ").upper()
            if user_input in alphabet - used_letters:
                used_letters.add(user_input)
                if user_input in valid_letters:
                    valid_letters.remove(user_input)
                else:
                    self.lives = self.lives - 1
            elif user_input in used_letters:
                print(
                    f"Letter {user_input} already used. Please choose another letter."
                )
            else:
                print("Invalid user input")

        if len(valid_letters) > 0 and self.lives == 0:
            print(f"You lost. The word was {word}")
        else:
            print(f"Yay, you guessed the word {word}")


if __name__ == "__main__":
    game = hangman_game(words, 6)
    secret_word = game.get_valid_word()
    game.play_hangman(secret_word)
