import pytest
from game import Game


class TestGame:
    # creates game then calls new round multiple times to ensure that the 
    # game state is reset correctly and that the new target word is valid
    def test_new_round_resets_game_state_with_valid_target(self):
        game = Game()

        all_words = game.word_list.get_all_words()

        for _ in range(50):
            game.new_round()
            assert game.attempts == 0
            assert game.won is False
            assert game.puzzle.target in all_words
