import Classes.Path as Path
import re

# Efficiency and memory cost should be paid with extra attention.
# Essential private methods or variables can be added.

# Please add comments along with your code.
class WordTokenizer:

    def __init__(self, content):
        # Tokenize the input texts.
        # For each document, the content is passed as an argument for this class.
        # This class sequentially reads words from a sequence of characters.

        # Using regex to to split the content into words - First, find words using regex
        self.words = re.findall(r'\b\w+\b', content)

        # Initialize index - keeps track of current word:
        self.index = 0

        return

    def nextWord(self):
        # Return the next word in the document.
        # Return null, if it is the end of the document.
        word = ""
        if self.index < len(self.words):
            # Get the next word
            word = self.words[self.index] 
            # Move to the next word for the next call
            self.index += 1 
            # Return the current word
            return word
        
        # If reached end of the document, return none.
        return None 
