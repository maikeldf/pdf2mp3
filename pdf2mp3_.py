import PyPDF2
import pyttsx3
from tkinter import Tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def main():
    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    pdf= Tk().clipboard_get()

    filelocation = askopenfilename(defaultextension=".pdf", filetypes=(("pdf file", "*.pdf"),("All Files", "*.*") ))
    if not filelocation:
        return

    # path of the PDF file
    path = open(filelocation, 'rb')
      
    # creating a PdfFileReader object
    pdfReader = PyPDF2.PdfFileReader(path)

    '''count = pdfReader.numPages
    text = []
    for i in range(count):
        page = pdfReader.getPage(i)
        text.append(page.extractText())
    '''
    # the page with which you want to start
    # this will read the page of 25th page.
    from_page = pdfReader.getPage(24)
      
    # extracting the text from the PDF
    text = from_page.extractText()
      
    # reading the text
    speak = pyttsx3.init()
    speak.say(text)
    speak.runAndWait()

if __name__ == "__main__":
    main()