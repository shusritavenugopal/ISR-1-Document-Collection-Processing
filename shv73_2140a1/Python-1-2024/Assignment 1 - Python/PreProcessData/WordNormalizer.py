import Classes.Path as Path
from nltk.stem import PorterStemmer

# Efficiency and memory cost should be paid with extra attention.
# Essential private methods or variables can be added.

# Please add comments along with your code.
class WordNormalizer:

    def __init__(self):
        # Initialize the stemmer - used to perform stemming on words.
        self.stemmer = PorterStemmer()

        # Initialize a lookup dictionary to cache results of previously stemmed words - avoids redundant computations for the same words.
        self.lookup = {}
        return

    def lowercase(self, word):
        # Converts the input word into lowercase - ensures transformations like stemming are case-insensitive.
        return word.lower()

    def stem(self, word):
        # Returns the stemmed version of the given word using the PorterStemmer.

        # If the word is in the cache, it returns the cached stemmed word, avoiding redundant computation.
        if word in self.lookup:
            return self.lookup[word]
        
        # If not in cache, stem the word and store it in the cache
        stemmed_word = self.stemmer.stem(word)

        # Cache the stemmed word for future reuse.
        self.lookup[word] = stemmed_word

        # Return the stemmed version of the word.
        return stemmed_word
