from bible_word_list import BibleWordList
from puzzle import Puzzle

class Game:
    def __init__(self):
        self.word_list = BibleWordList()
        self.max_attempts = 6
        self.new_round()

    def new_round(self):
        target = self.word_list.get_random_word()
        self.puzzle = Puzzle(target)
        self.attempts = 0
        self.won = False

    def play(self):
        print("Welcome to Bible Wordle!")
        print("Guess the 5-letter Bible Character name in 6 tries.")
        print("🟩 = correct letter & position")
        print("🟨 = correct letter, wrong position")
        print("⬜ = not in word\n")

        while self.attempts < self.max_attempts:
            guess = self._get_valid_guess()

            if guess == "QUIT":
                print("Thanks for playing! Goodbye!")
                return
            
            feedback = self.puzzle.generate_feedback(guess)
            print(f"Guess {self.attempts + 1}/{self.max_attempts}: {guess}")
            print(f"{feedback}\n")
            self.attempts += 1

            if guess == self.puzzle.target:
                print(f"Correct! The word was {self.puzzle.target}")
                print(f"You won in {self.attempts} attempt{'s' if self.attempts > 1 else ''}!")
                self.won = True
                break
        
        if not self.won:
            print(f"Game Over! The word was {self.puzzle.target}")

        while True:
            replay = input("\nPlay again? (Y/N): ").strip().upper()
            if replay in ("Y", "YES"):
                self.new_round()
                self.play()
                return
            elif replay in ("N", "NO", ""):
                print("Thanks for playing!")
                return
            else:
                print("Please enter Y or N.")

    def _get_valid_guess(self):
        while True:
            guess = input (f"Guess #{self.attempts +1}/{self.max_attempts}: ").strip().upper()

            if guess == "QUIT":
                return "QUIT"
            
            if len(guess) == 0:
                print("Please enter a guess.")
                continue

            if len(guess) != 5:
                print("Please enter a 5-letter word.")
                continue

            if not guess.isalpha():
                print("Please enter only letters.")
                continue

            if not self.word_list.is_valid(guess):
                print("Not a valid Bible character name. Try again.")
                continue

            return guess
        