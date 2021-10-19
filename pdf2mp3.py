import argparse
import pdftotext
from gtts import gTTS
from tkinter import Tk
from pydub import AudioSegment
from pydub.playback import play
from tkinter.filedialog import askopenfilename, asksaveasfilename

def run(arg= ""):
    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing

    pdf= Tk().clipboard_get()

    if not arg:
        filelocation = askopenfilename(defaultextension=".pdf", filetypes=(("pdf file", "*.pdf"),("All Files", "*.*") ))
        if not filelocation:
            return    

        with open(filelocation, "rb") as f:  # open the file in reading (rb) mode and call it f
            pdf = pdftotext.PDF(f)  # store a text version of the pdf file f in pdf variable
    elif not pdf:
        print("Empty")
        return

    string_of_text = pdf.replace("\n", "")
    print(string_of_text)

    final_file = gTTS(text=string_of_text, lang='en-us')  # pt-br, check language support gtts.lang.tts_langs()
    
    filename = "GeneratedSpeech.mp3"
    if not arg:
        filename = asksaveasfilename(defaultextension=".mp3", filetypes=(("mp3 file", "*.mp3"),("All Files", "*.*") ))


    final_file.save(filename)  # save file to computer
    
    audio = AudioSegment.from_mp3(filename)
    play(audio)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--clipboard", help="Converts form clipboard")
    args = parser.parse_args()
    if args.clipboard:
        run(args.clipboard)
    else:
        run()