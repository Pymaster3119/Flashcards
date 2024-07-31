import tkinter
import main
import pickle
import random
root = tkinter.Tk()
outputvar = tkinter.StringVar(root)
#REPLACE
setname = input("What set do you want?: ")
with open(setname, "rb") as txt:
    set = pickle.load(txt)

set = random.shuffle(set)
idx = 0
def showterm():
    outputvar = "What is meant by" + set[idx].term
tkinter.Label(root, textvariable=outputvar).pack()
root.mainloop()