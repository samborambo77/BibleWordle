import random

class BibleWordList:
    def __init__(self):
        self.words = {
            "AARON", "ABNER", "ABRAM", "ADIEL", "AMASA", "AMMON", "AMNON",
            "AMRAM", "ANNAS", "ARIEL", "ASAPH", "ASHER", "BALAK", "BARAK",
            "CALEB", "CHLOE", "CYRUS", "DAVID", "ELIAS", "ENOCH", "GOMER",
            "HAGAR", "HEROD", "HIRAM", "ISAAC", "JACOB", "JAMES", "JARED",
            "JASON", "JESUS", "JOASH", "JONAH", "KORAH", "LYDIA", "MICAH",
            "MOSES", "NAOMI", "PETER", "RAHAB", "RHODA", "SARAH", "SILAS",
            "SIMON", "TAMAR", "TITUS", "URIAH", "ZEBUL"
        }

        self.word_set = set(self.words) #making it a set for faster lookup

    def get_random_word(self):
        return random.choice(list(self.word_set))
    
    def is_valid(self, word):
        return len(word) == 5 and word.isalpha() and word in self.word_set
    
    def get_all_words(self):
        return sorted(self.word_set) # returns a sorted list of all the words in the set
        # making sure the list is there and words are what we expect    
    def __len__(self):
        return len(self.word_set) #gives the total number of words in the list
