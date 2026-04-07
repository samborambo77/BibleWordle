class Puzzle:
    def __init__(self, target):
        self.target = target.upper()
        # These are the emoji symbols for the game
        self.symbols = {
            "correct": "🟩", 
            "present": "🟨", 
            "absent": "⬜"
        }

    def generate_feedback(self, guess):
        guess = guess.upper()
        
        # Safety check to make sure the guess is exactly 5 letters
        if len(guess) != 5:
            return "⬜⬜⬜⬜⬜"
            
        result = [""] * 5 # build the result as a list then make it a string
        
        # Make counters for accurate duplicate handling
        from collections import Counter
        target_count = Counter(self.target)

        # STEP 1: Look for exact matches (Green)
        for i in range(5):
            if guess[i] == self.target[i]:
                result[i] = self.symbols["correct"]
                target_count[guess[i]] -= 1

        # STEP 2: mark yellows and grays
        for i in range(5):
            if result[i] == "":  # Not already marked as green
                if guess[i] in target_count and target_count[guess[i]] > 0:
                    result[i] = self.symbols["present"]
                    target_count[guess[i]] -= 1
                else:
                    result[i] = self.symbols["absent"]
        
        return "".join(result)