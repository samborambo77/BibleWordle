# Bible Wordle

Welcome to **Bible Wordle**! This is a Wordle-inspired game where you have 6 chances to guess a 5-letter Bible character's name. 

You can play this game in two different ways:
1. A modern graphical user interface (GUI) built with `customtkinter`.
2. A classic text-based terminal version.

## Installation

To play the graphical version of the game, you will need to install **CustomTkinter**, which is a modern UI library for Python.

1. Open your terminal or command prompt.
2. Install CustomTkinter using pip by running:
   ```bash
   pip install customtkinter
   ```
*(Note: You may need to use `pip3` instead of `pip` depending on your Mac/Linux setup).*

## How to Boot Up the Game

First, open your terminal and navigate to the project folder:
```bash
cd /Users/User/Documents/BibleWordle
```

### Play the GUI Version (Recommended)
To launch the visual game with the interactive grid:
```bash
python3 wordle_gui.py
```

### Play the Terminal Version
To play the text-based version directly in your terminal:
```bash
python3 main.py
```

## How to Play
- Type a 5-letter Bible character name and press **Enter**.
- 🟩 **Green**: The letter is in the word and in the correct spot.
- 🟨 **Yellow**: The letter is in the word but in the wrong spot.
- ⬜ **Gray**: The letter is not in the word at all.