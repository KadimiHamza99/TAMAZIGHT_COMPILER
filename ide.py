from tkinter import *
from TamazightLexerParser import parser

window = Tk()
window.title('T++ IDE')
window.geometry('900x850')
window.config()


def RunCode():
    print("Execution ...")
    code = textEditor.get('1.0', END)
    parser.parse(code)


textEditor = Text(window, highlightcolor = 'green', highlightbackground='green', fg='#c0c2e8', bg='#13153d',height=26, font=("verdana", 15))
textEditor.pack()

button = Button(window, text='ⵣⵣⴳⵔ - Run', command=RunCode, bg='green')
button.pack(pady=5)

window.mainloop()
