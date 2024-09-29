import Classes.Path as Path
import re

# Efficiency and memory cost should be paid with extra attention.
# Essential private methods or variables can be added.

# Please add comments along with your code.
class TrectextCollection:

    def __init__(self):
        # 1. Open the file in Path.DataTextDir.
        # 2. Make preparation for function nextDocument().
        # NOTE: you cannot load the whole corpus into memory!!

        # Path.DataTextDir holds the location of the given docset.trectext file
        self.file_path = Path.DataTextDir

        # Open the file in read mode to process document by document, avoiding loading the entire file into memory at once.
        self.file = open(self.file_path, 'r', encoding='utf-8')

        # Initialize a flag to track the end of the file: Initially set to false to indicate the document end is not reached.
        self.reached_end = False

        return

    def nextDocument(self):
        # 1. When called, this API processes one document from corpus, and returns its doc number and content.
        # 2. When no document left, return null, and close the file.
        
        # If the end of the file was already reached in a previous call, return None
        if self.reached_end:
            return None
        
        # Initializing given variables to store the document number and content
        docNo = ""
        content = ""

        # Boolean flag to track whether we're inside a <TEXT> block.
        inside_text = False

        # Iterate over each line in the file, reading one line at a time
        for line in self.file:
            line = line.strip()

            if line == "<DOC>":
                # Beginning of a new document, reset docNo and content for this new doc.
                docNo = ""
                content = ""
                inside_text = False

            elif line == "</DOC>":
                # if end of the current document, return the docNo and content
                if docNo != "" and content != "":
                    return [docNo, content.strip()]
                else:
                    # if the document is incomplete (missing docNo/content), skip to the next document
                    continue

            elif line.startswith("<DOCNO>"):
                # Extract the docNo from <DOCNO></DOCNO> using regex
                docNo = re.search(r"<DOCNO>(.*?)</DOCNO>", line).group(1).strip()

            elif line.startswith("<TEXT>"):
                # Start of a <TEXT> block, meaning the content of the document begins here
                inside_text = True
                # Add the content from the same line without the <TEXT> tag
                content += line.replace("<TEXT>", "").strip() + " "

            elif line.endswith("</TEXT>"):
                # end of a <TEXT> block, meaning the content of the document ends here
                content += line.replace("</TEXT>", "").strip() + " "
                # update the flag to False as we reached the </TEXT> block
                inside_text = False

            elif inside_text:
                # If we are inside a <TEXT> block, append the current line to the content
                content += line + " "

        # If the end of the file is reached, close the file and set the reached_end flag
        self.reached_end = True
        self.file.close()
        return None