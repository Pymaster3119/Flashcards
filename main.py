import os
import pygame
from tkinter import *
def playSound(sound):
    pygame.mixer.music.load(os.getcwd() + "/" + sound)
    pygame.mixer.music.play(loops=0)

class Flashcard:
    def __init__(self, term, definition):
        self.term = term
        self.definition = definition

def runapp(app, root):
    for child in root.winfo_children():
        child.destroy()
    app.runapp(root)

def render(root):
    for child in root.winfo_children():
        child.destroy()
    Button(root, text="Add Flashcards", command=lambda: runapp(addflashcards, root)).pack()
    Button(root, text="Quiz Flashcards", command=lambda: runapp(loadflashcards, root)).pack()

if __name__ == "__main__":
    import addflashcards
    import loadflashcards
    root = Tk()
    render(root)
    root.mainloop()