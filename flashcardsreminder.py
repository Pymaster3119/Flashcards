import main
from tkinter import *
import pickle
import datetime

root = Tk()

#REPLACE
setname = input("What set do u want?: ")

#Find dates and clean list
with open("studytimes/" + setname, "rb") as txt:
    list = pickle.load(txt)
for i in list:
    try:
        print((list[i] - list[i+1]))
        if (list[i] - list[i+1]).day < 1:
            list.remove(i)
    except:
        pass

print(list)
deltas = main.generateStudyDifferences(100)
print(deltas)
delta = deltas[len(list)]

Label(root, text="You have to study in: " + str(delta) + " days").pack()
root.mainloop()