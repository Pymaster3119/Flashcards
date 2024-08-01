import os
import pygame
from tkinter import *

import pygame.mixer_music
def playSound(sound):
    pygame.mixer.init()
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

def generateStudyDifferences(n):
    sequence = [1, 2, 4, 9, 14]
    differences = [1, 2, 5, 5]
    
    while len(sequence) < n:
        next_diff = differences[-1] + (differences[-1] - differences[-2]) if len(differences) > 1 else differences[-1] + 1
        next_term = sequence[-1] + next_diff
        sequence.append(next_term)
        differences.append(next_diff)
    
    return sequence

if __name__ == "__main__":
    import addflashcards
    import loadflashcards
    root = Tk()
    render(root)
    root.mainloop()