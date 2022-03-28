import sys
import pytesseract
from googletrans import Translator
import pytesseract
from imageLocation import imgRead
import pyperclip as pc

def copyText(language):
    pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
    #Set language to be translated, and what format the text is in
    config = "-l "+language+" --psm 3"
    text = pytesseract.image_to_string(imgRead(), config=config)
    #For some special characters to be able to print
    encode = text.encode('utf-8')
    nativeLang = sys.stdout.buffer.write(encode)
    pc.copy(text)
    print(nativeLang)
    return nativeLang

def translate(nativeLang):
        #Uses google API to translate text
    translator = Translator()
    translation = translator.translate(nativeLang, dest='en')
    print(translation.text)
    pc.copy(translation.text)
    return translation.text