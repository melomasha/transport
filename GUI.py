__author__ = 'maria'
from tkinter import *
import sys
from parserHTML import ParserHTML

def PrintLetter():
    r = letter.get()
    ss = ParserHTML()
    trams = ss.parseTrams()
    if trams.get(r):
        print(trams[r])
    else:
        print(r)



root = Tk()
root.title("First letter")
root.geometry('300x300')
quest = Label(root, text="Введите первую букву остановки")
butOk = Button(root, text="Ok", bg = 'gold', command = PrintLetter)
letter = Entry(root)
quest.pack()
letter.pack()
butOk.pack()
root.mainloop()