class Puzzle:
    def __init__(self, target):
        self.target = target.upper()
        # These are the emoji symbols for the game
        self.feedback_symbols = {
            "correct": "🟩", 
            "present": "🟨", 
            "absent": "⬜"
        }

    def generate_feedback(self, guess):
        guess = guess.upper()
        
        # Safety check to make sure the guess is exactly 5 letters
        if len(guess) != 5:
            return [""] * 5
            
        # Start with 5 empty spots for our results
        result = [""] * 5
        
        # We make a list of the target letters so we can "check them off"
        target_letters = list(self.target)
        # We also make a list of the guess letters
        guess_letters = list(guess)

        # STEP 1: Look for exact matches (Green)
        for i in range(5):
            if guess_letters[i] == target_letters[i]:
                result[i] = self.feedback_symbols["correct"]
                # Mark these as "None" so we don't count them again in Step 2
                target_letters[i] = None
                guess_letters[i] = None

        # STEP 2: Look for letters that are in the word but wrong spot (Yellow)
        for i in range(5):
            # Only check if we didn't already find a Green match here
            if guess_letters[i] is not None:
                if guess_letters[i] in target_letters:
                    result[i] = self.feedback_symbols["present"]
                    # Find where that letter is in the target and remove it
                    index = target_letters.index(guess_letters[i])
                    target_letters[index] = None
                else:
                    # If it's not in the target at all, it's Gray
                    result[i] = self.feedback_symbols["absent"]
        
        return result