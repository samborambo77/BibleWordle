import unittest
from BibleWordleApp import BibleWordleApp
# This is AI generated 
# A simple fake event class to trick our app into thinking a key was pressed
class FakeEvent:
    def __init__(self, keysym="", char=""):
        self.keysym = keysym
        self.char = char

class TestBibleWordleApp(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        # Creates the window EXACTLY ONCE for all tests. 
        # Doing this prevents the "TclError" or window crashing errors!
        cls.app = BibleWordleApp()
        
    @classmethod
    def tearDownClass(cls):
        # Destroys the window ONLY when all 5 tests are totally finished
        cls.app.destroy()

    def setUp(self):
        # This runs before EVERY test to clear the board to a blank slate
        self.app.reset_game()
        self.app.game_started = False

    def test_initial_state(self):
        # Test 1: Check that the game starts at row 0, col 0, and isn't playing yet
        self.assertEqual(self.app.current_row, 0)
        self.assertEqual(self.app.current_col, 0)
        self.assertFalse(self.app.game_started)

    def test_start_game(self):
        # Test 2: Check that calling start_game() allows typing
        self.app.start_game()
        self.assertTrue(self.app.game_started)

    def test_typing_letter(self):
        # Test 3: Check that typing a letter moves the column tracker forward by 1
        self.app.start_game()  # Start the game to allow typing
        
        fake_key = FakeEvent(char="d")  # Simulate typing the letter 'd'
        self.app.handle_keypress(fake_key)
        
        self.assertEqual(self.app.current_col, 1)
        # Make sure it capitalized the letter on the screen widget
        self.assertEqual(self.app.cells[0][0].cget("text"), "D")

    def test_backspace_letter(self):
        # Test 4: Check that Backspace deletes the letter and moves the tracker back
        self.app.start_game()
        
        # Type a letter first so we have something to delete
        self.app.handle_keypress(FakeEvent(char="a"))
        self.assertEqual(self.app.current_col, 1)  # Verify we moved forward
        
        # Now simulate pressing Backspace
        self.app.handle_keypress(FakeEvent(keysym="BackSpace"))
        self.assertEqual(self.app.current_col, 0)  # Verify we moved backward
        self.assertEqual(self.app.cells[0][0].cget("text"), "")  # Verify the letter was erased

    def test_reset_game(self):
        # Test 5: Check that resetting puts our trackers back to the very beginning
        self.app.start_game()
        
        # Fake that the user has played a few rounds
        self.app.current_row = 4
        self.app.current_col = 3
        
        self.app.reset_game()
        
        # Verify it reset to zero
        self.assertEqual(self.app.current_row, 0)
        self.assertEqual(self.app.current_col, 0)

if __name__ == "__main__":
    unittest.main()
