import Classes.Path as Path

# Efficiency and memory cost should be paid with extra attention.
# Essential private methods or variables can be added.

# Please add comments along with your code.
class StopWordRemover:

    def __init__(self):
        # Load and store the stop words from the fileinputstream with appropriate data structure.
        # NT: address of stopword.txt is Path.StopwordDir.

        self.stopwords = set()
        self.load_stopwords()

        return
    
    def load_stopwords(self):
        # Reading the given stpword file to store them in a set "stopwords"
        with open(Path.StopwordDir, 'r', encoding='utf-8') as f:
            for line in f:
                # Removing whitespaces and adding the stopwords to the set
                self.stopwords.add(line.strip().lower())

    def isStopword(self, word):
        # Return true if the input word is a stopword, or false if not
        return word.lower() in self.stopwords
