# importing the modules
import PyPDF2
import pyttsx3


class PDFReader:
    def __init__(self, file_path):
        # path of the PDF file
        self.path = open(file_path)

    def translate_pdf(self):
        # creating a PdfFileReader object
        pdf_reader = PyPDF2.PdfFileReader(self.path)

        # the page with which you want to start
        # this will read the book of 25th page.
        from_page = pdf_reader.getPage(30)

        # extracting the text from the PDF
        entry_text = from_page.extractText()

        return str(entry_text)

    # reading the text
    # speak = pyttsx3.init()
    # speak.say(entry_text)
    # speak.runAndWait()