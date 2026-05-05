import random

class BibleWordList:
    def __init__(self):
        self.words = {
            "AARON", "ABDON", "ABIAH", "ABIHU", "ABNER", "ABRAM", "AMASA", "AMMON","AMRAM", 
            "ANNAS", "ARIEL", "ASAPH", "ASHER", "ASHUR", "ASSUR", "BALAK", "CALEB",
            "CHLOE", "CYRUS", "DAVID", "DINAH", "ELIAB", "ELIAS", "ELIHU", "ENOCH", "FELIX",
            "GAIUS", "HAGAR", "HAMAN", "HEROD", "HIRAM", "HOSEA", "ISAAC", "JABEZ", "JACOB",
            "JAMES", "JASON", "JESSE", "JESUS", "JOASH", "JONAH", "JONAS", "JORAM", "JOSES",
            "JUBAL", "JUDAH", "JUDAS", "KORAH", "LABAN", "LYDIA", "MICAH", "MOSES",
            "NABAL", "NADAB", "NAHUM", "NAOMI", "ORNAN", "ORPHA", "PEKAH", "PETER",
            "PHEBE", "RAHAB", "REHUM", "REZIN", "RHODA", "RUFUS", "SARAH", "SARAI",
            "SHAUL", "SIHON", "SILAS", "SIMON", "TAMAR", "TITUS", "TUBAL", "URIAH",
            "ZADOK", "ZARAH", "ZEBUL", "ZIMRI"
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
