import pytest
from bible_word_list import BibleWordList


class TestBibleWordList:
    @pytest.fixture
    def word_list(self):
        return BibleWordList()

#testing the is_valid method to ensure it correctly identifies valid and invalid words
    def test_is_valid_validates_words_correctly(self, word_list):
        valid = word_list.get_random_word()
        assert word_list.is_valid(valid)

        assert not word_list.is_valid("APPLE")
        assert not word_list.is_valid("MOSESS")
        assert not word_list.is_valid("MOS")
        assert not word_list.is_valid("MOSE$")
        assert not word_list.is_valid("")

# testing the get_all_words method to ensure it returns a sorted list of all words in the set
    def test_get_random_word_returns_word_from_set(self, word_list):
        words_seen = set()
        for _ in range(200):
            word = word_list.get_random_word()
            assert word in word_list.word_set
            words_seen.add(word)
        assert len(words_seen) > 1
