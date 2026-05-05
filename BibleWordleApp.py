import customtkinter as ctk
from bible_word_list import BibleWordList
from puzzle import Puzzle

class BibleWordleApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # --- Window Setup ---
        self.title("Bible Wordle")
        self.geometry("500x600")

        # --- Initialize Game Backend ---
        # This grabs our logic from the other files so we don't have to rewrite it
        self.word_list = BibleWordList()
        self.target_word = self.word_list.get_random_word()
        self.puzzle = Puzzle(self.target_word)

        # --- Game State Variables ---
        # These track where the user is currently typing
        self.current_row = 0
        self.current_col = 0
        self.cells = []  # This will hold all 30 label widgets for easy access later
        self.game_started = False  # Prevents typing before the game starts

        # --- Create Basic UI Elements ---
        self.title_label = ctk.CTkLabel(self, text="Bible Wordle", font=ctk.CTkFont(size=32, weight="bold"))
        self.title_label.pack(pady=(40, 20))

        # --- Start Screen Elements ---
        instructions = (
            "How to Play:\n\n"
            "1. Guess the 5-letter Bible character in 6 tries.\n"
            "2. Type your guess and press Enter.\n\n"
            "Color Code:"
        )
        self.instructions_label = ctk.CTkLabel(self, text=instructions, font=ctk.CTkFont(size=16), justify="left")
        self.instructions_label.pack(pady=(20, 5))

        # --- Custom Color Legend ---
        self.legend_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.legend_frame.pack(pady=5)

        # Green Box
        ctk.CTkLabel(self.legend_frame, text="", width=24, height=24, fg_color="#538d4e", corner_radius=4).grid(row=0, column=0, padx=10, pady=2)
        ctk.CTkLabel(self.legend_frame, text="Correct letter & position", font=ctk.CTkFont(size=14)).grid(row=0, column=1, sticky="w")

        # Yellow Box
        ctk.CTkLabel(self.legend_frame, text="", width=24, height=24, fg_color="#b59f3b", corner_radius=4).grid(row=1, column=0, padx=10, pady=2)
        ctk.CTkLabel(self.legend_frame, text="Correct letter, wrong position", font=ctk.CTkFont(size=14)).grid(row=1, column=1, sticky="w")

        # Gray Box
        ctk.CTkLabel(self.legend_frame, text="", width=24, height=24, fg_color="#3a3a3c", corner_radius=4).grid(row=2, column=0, padx=10, pady=2)
        ctk.CTkLabel(self.legend_frame, text="Letter not in the word", font=ctk.CTkFont(size=14)).grid(row=2, column=1, sticky="w")

        self.start_btn = ctk.CTkButton(self, text="Start Game", font=ctk.CTkFont(size=20, weight="bold"), command=self.start_game)
        self.start_btn.pack(pady=20)

        # --- Game Screen Elements (Created but NOT packed yet) ---
        self.info_label = ctk.CTkLabel(self, text="Type a 5-letter Bible word and press Enter!", font=ctk.CTkFont(size=16))

        # --- Create the 6x5 Wordle Grid ---
        self.grid_frame = ctk.CTkFrame(self, fg_color="transparent")
        
        # Loop 6 times for rows, and 5 times inside that for columns
        for row in range(6):
            row_cells = []
            for col in range(5):
                # Create a single empty box (label)
                cell = ctk.CTkLabel(self.grid_frame, text="", width=60, height=60,
                                    font=ctk.CTkFont(size=30, weight="bold"),
                                    fg_color=("gray75", "gray25"), corner_radius=8)
                # Place it in the grid using row and column coordinates
                cell.grid(row=row, column=col, padx=5, pady=5)
                row_cells.append(cell)
            self.cells.append(row_cells)

        # Label to show error messages or win/loss text
        self.result_label = ctk.CTkLabel(self, text="", font=ctk.CTkFont(size=16))

        self.play_again_btn = ctk.CTkButton(self, text="Play Again", command=self.reset_game)
        # We will only pack (show) this button when the game ends

        # --- Action Buttons (Restart & Quit) ---
        self.action_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.restart_btn = ctk.CTkButton(self.action_frame, text="Restart", width=120, command=self.reset_game)
        self.restart_btn.pack(side="left", padx=10)
        
        self.quit_btn = ctk.CTkButton(self.action_frame, text="Quit", width=120, command=self.destroy)
        self.quit_btn.pack(side="right", padx=10)

        # --- Bind Physical Keyboard Events ---
        # Tells the app to run 'handle_keypress' whenever ANY key is pressed
        self.bind("<Key>", self.handle_keypress)

    def start_game(self):
        # Hide the start screen elements
        self.instructions_label.pack_forget()
        self.legend_frame.pack_forget()
        self.start_btn.pack_forget()
        
        # Show the game screen elements
        self.info_label.pack(pady=(0, 20))
        self.grid_frame.pack(pady=10)
        self.result_label.pack(pady=30)
        self.action_frame.pack(pady=10)
        
        # Allow typing
        self.game_started = True

    def handle_keypress(self, event):
        if not self.game_started:
            return  # Ignore key presses if the user is still on the start screen
            
        if self.current_row >= 6:
            return  # The game is already over
            
        # If the user hits Backspace, move back one column and erase the letter
        if event.keysym == "BackSpace":
            if self.current_col > 0:
                self.current_col -= 1
                self.cells[self.current_row][self.current_col].configure(text="")
                self.result_label.configure(text="")  # Clear any error messages
        # If the user hits Enter (Return), check the guess if the row is full
        elif event.keysym == "Return":
            if self.current_col == 5:
                self.check_guess()
            else:
                self.result_label.configure(text="Not enough letters!", text_color="orange")
        # If the user types a normal letter, add it to the current box
        elif event.char.isalpha() and len(event.char) == 1:
            if self.current_col < 5:
                self.cells[self.current_row][self.current_col].configure(text=event.char.upper())
                self.current_col += 1
                self.result_label.configure(text="")  # Clear any error messages

    def check_guess(self):
        # Combine letters from the current row to make the guess word
        guess = ""
        for col in range(5):
            # .cget("text") reads the current text inside the label widget
            letter = self.cells[self.current_row][col].cget("text")
            guess += letter
        
        # Validate the word using our backend list
        if not self.word_list.is_valid(guess):
            self.result_label.configure(text="Not a valid Bible character name.", text_color="red")
            return
        
        # Get the emoji feedback string (e.g., "🟩🟨⬜⬜🟩") from puzzle.py
        feedback = self.puzzle.generate_feedback(guess)
        
        # Color the tiles based on the emojis returned by the Puzzle class
        for col in range(5):
            emoji = feedback[col]
            if emoji == "🟩":
                color = "#538d4e"  # Wordle Green
            elif emoji == "🟨":
                color = "#b59f3b"  # Wordle Yellow
            else:
                color = "#3a3a3c"  # Wordle Dark Gray
                
            # Apply the color to the specific box
            self.cells[self.current_row][col].configure(fg_color=color, text_color="white")

        # --- Win/Loss Logic ---
        if guess == self.target_word:
            self.result_label.configure(text="Correct! You won!", text_color="green")
            self.current_row = 6  # Stop gameplay
            self.play_again_btn.pack(pady=10)
        else:
            # Move to the next row for the next guess
            self.current_row += 1
            self.current_col = 0
            
            # If they just finished the 6th row, they lost
            if self.current_row >= 6:
                self.result_label.configure(text=f"Game Over! The word was {self.target_word}", text_color="red")
                self.play_again_btn.pack(pady=10)

    def reset_game(self):
        self.play_again_btn.pack_forget()  # Hide the button again
        
        # Reset backend variables for a new round
        self.target_word = self.word_list.get_random_word()
        self.puzzle = Puzzle(self.target_word)
        self.current_row = 0
        self.current_col = 0
        self.result_label.configure(text="")
        
        # Clear the visual grid colors and text
        for row in range(6):
            for col in range(5):
                self.cells[row][col].configure(text="", fg_color=("gray75", "gray25"))

if __name__ == "__main__":
    ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
    ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
    app = BibleWordleApp()
    app.mainloop()