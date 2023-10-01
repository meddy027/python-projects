import random


class PlayerNumberGame:
    def __init__(self, min_range, max_range):
        # range 10 to 100 numbers
        self.num_range = random.randint(min_range, max_range)
        self.secret_number = random.randint(1, self.num_range)
        self.tries = 0

    def get_guess(self):
        return int(input("Guess a number: "))

    def play(self):
        print(f"I am thinking of a number between 1 and {self.num_range}.")
        print("Guess the number and you will win the game.")

        while True:
            guess = self.get_guess()
            self.tries += 1

            if guess < self.secret_number:
                print("Guess too low. Guess again.")
            elif guess > self.secret_number:
                print("Guess too high. Guess again.")
            else:
                print(
                    f"Congratulations! You guessed the secret number {self.secret_number} in {self.tries} tries."
                )
                break


class ComputerNumberGame:
    def computerGuess(self, low, high):
        while low <= high:
            mid = (low + high) // 2
            print(f"I guess {mid}")
            feedback = input("Was guess too low [L], too high [H], or correct [C]? ")
            if feedback.upper() == "C":
                print("Yay I guessed the number!")
                break
            elif feedback.upper() == "L":
                low = mid + 1
            elif feedback.upper() == "H":
                high = mid - 1


if __name__ == "__main__":
    # min_range = 10
    # max_range = 100
    # game = PlayerNumberGame(min_range, max_range)
    # game.play()

    low_number = int(input("Please enter bottom bound: "))
    high_number = int(input("Please enter upper bound: "))
    computerGame = ComputerNumberGame()
    computerGame.computerGuess(low_number, high_number)
