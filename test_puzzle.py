import pytest
from puzzle import Puzzle


class TestPuzzle:
    # testing the colors to make sure they are correct
    def test_generate_feedback_basic_scenarios(self):
        p = Puzzle("MOSES")

        assert p.generate_feedback("MOSES") == "🟩🟩🟩🟩🟩"
        assert p.generate_feedback("CURLY") == "⬜⬜⬜⬜⬜"
        assert p.generate_feedback("MOOSE") == "🟩🟩⬜🟨🟨"
        assert p.generate_feedback("SMOKE") == "🟨🟨🟨⬜🟨"
    # testing the duplicate letters to make sure they are handled correctly
    def test_generate_feedback_handles_duplicates_correctly(self):
        p = Puzzle("AARON")
        assert p.generate_feedback("AAABB") == "🟩🟩⬜⬜⬜"

        p2 = Puzzle("ANNAS")
        assert p2.generate_feedback("AAAAA") == "🟩⬜⬜🟩⬜"
        assert p2.generate_feedback("SANAA") == "🟨🟨🟩🟩⬜"
        assert p2.generate_feedback("NANAS") == "🟨🟨🟩🟩🟩"
