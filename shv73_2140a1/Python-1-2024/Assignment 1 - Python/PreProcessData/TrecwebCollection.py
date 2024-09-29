import Classes.Path as Path
import re

class TrecwebCollection:

    def __init__(self):
        try:
            # Open the file at Path.DataWebDir
            self.file_path = Path.DataWebDir
            self.file = open(self.file_path, 'r', encoding='utf-8')
            self.reached_end = False
        except FileNotFoundError:
            print(f"Error: The file at {self.file_path} was not found.")
            self.reached_end = True
        except Exception as e:
            print(f"An error occurred while opening the file: {e}")
            self.reached_end = True
        return

    def nextDocument(self):
        if self.reached_end:
            return None

        docNo = ""
        content = ""
        inside_content = False
        inside_doc = False  # Track whether we are inside a <DOC> tag

        try:
            for line in self.file:
                line = line.strip()

                # Detect the start of a new document
                if line == "<DOC>":
                    if inside_doc:
                        # If we encounter a new <DOC> without a closing </DOC>, handle the error
                        print("Error: Encountered a new <DOC> without closing the previous document.")
                        return None
                    inside_doc = True  # Mark that we are now inside a document
                    docNo = ""
                    content = ""
                    inside_content = False

                # Extract the document number
                elif line.startswith("<DOCNO>") and inside_doc:
                    docNo = re.search(r"<DOCNO>(.*?)</DOCNO>", line)
                    if docNo:
                        docNo = docNo.group(1).strip()
                    else:
                        print("Error: <DOCNO> tag is malformed.")
                        continue  # Skip to the next document if there's an issue with DOCNO

                # End of document header, start of content
                elif line == "</DOCHDR>" and inside_doc:
                    inside_content = True

                # End of the current document
                elif line == "</DOC>":
                    if inside_doc:
                        cleaned_content = self.clean_html(content)
                        inside_doc = False  # Mark that we've finished processing the current document
                        return [docNo, ' '.join(cleaned_content.split())]
                    else:
                        print("Error: Encountered </DOC> without a starting <DOC>.")
                        continue

                # Collect document content if inside <DOC> and after the </DOCHDR>
                elif inside_content and inside_doc:
                    content += line + " "

            # If we finish the file and haven't properly closed the document with </DOC>, handle the error
            if inside_doc:
                print("Error: File ended without closing a <DOC> with </DOC>.")

        except Exception as e:
            print(f"Error while processing the document: {e}")
            self.reached_end = True

        self.reached_end = True
        self.file.close()
        return None

    # Remove HTML tags from the text
    def clean_html(self, text):
        try:
            clean = re.compile('<.*?>')
            return re.sub(clean, '', text)
        except Exception as e:
            print(f"Error while cleaning HTML content: {e}")
            return text
