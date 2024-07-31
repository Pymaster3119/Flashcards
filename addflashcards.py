from tkinter import *
import pickle
import main
import tkscrolledframe

def createflashcard():
    global rownum, flashcards
    flashcards.append(Flashcardrow(entryframe, rownum))
    rownum += 1
    entryframe._resize_interior()

def savefile():
    with open(cardsetname.get(), "wb") as txt:
        flashcardsexport = []
        for flashcard in flashcards:
            flashcardsexport.append(flashcard.compress())
        pickle.dump(flashcardsexport, txt)

class Flashcardrow:
    def __init__(self, root, rownum):
        self.termvar = StringVar(root)
        self.definitionvar = StringVar(root)
        Label(root, text="Term:").grid(row = rownum, column=0)
        Entry(root, textvariable=self.termvar).grid(row=rownum,column=1)
        Label(root, text="Definition:").grid(row = rownum, column=2)
        Entry(root, textvariable=self.definitionvar).grid(row=rownum,column=3)
    def compress(self):
        self.termvar = self.termvar.get()
        self.definitionvar = self.definitionvar.get()
        return main.Flashcard(self.termvar, self.definitionvar)

root = Tk()
cardsetname = StringVar(root)
frame = Frame(root)
frame.pack()
Label(frame, text="What is the name of your set:").grid(row= 0, column=0)
Entry(frame, textvariable=cardsetname).grid(row = 0, column= 1)
entryframe = tkscrolledframe.ScrolledFrame(frame)
entryframe.grid(row=2, column = 0, columnspan=2)
Button(frame, text="Create Flashcard", command=createflashcard).grid(row=3, column=0)
Button(frame, text="Save Set", command=savefile).grid(row=3, column=1)
rownum = 0
flashcards = []

root.mainloop()