from tkinter import *
from TamazightLexerParser import parser

window = Tk()
window.title('T++ IDE')

def RunCode():
    print("Execution ...")
    code = textEditor.get('1.0',END)
    parser.parse(code)

textEditor = Text()
textEditor.pack()

button = Button(window,text = 'ⵣⵣⴳⵔ - Run', command=RunCode)
button.pack()

window.mainloop()