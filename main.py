import os
import pygame

def playSound(sound):
    pygame.mixer.music.load(os.getcwd() + "/" + sound)
    pygame.mixer.music.play(loops=0)

class Flashcard:
    def __init__(self, term, definition):
        self.term = term
        self.definition = definition