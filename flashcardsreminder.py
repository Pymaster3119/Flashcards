import main
from tkinter import *
import pickle
import datetime

setname = None

def runUI():
    #Find dates and clean list
    with open("studytimes/" + setname.get(), "rb") as txt:
        list = pickle.load(txt)
    for i in range(len(list)):
        try:
            print((list[i] - list[i+1]).days)
            if (list[i] - list[i+1]).days < 1:
                list.remove(list[i])
        except:
            pass

    print(list)
    deltas = main.generateStudyDifferences(100)
    print(deltas)
    delta = deltas[len(list)]
    try:
        delta = delta - (datetime.datetime.now() - list[len(list)-1]).days
    except:
        pass

    Label(root, text="You have to study" + setname.get() + "next in: " + str(delta) + " days").pack()

def runapp(root):
    setname = StringVar()
    with open("flashcardsnames", "r") as txt:
        sets = txt.read().split("\n")
        setname.set(sets[0])
    OptionMenu(root, setname, *sets).pack()
    Button(root, text="See Schedule", command=runUI).pack()

if __name__ == "__main__":
    root = Tk()
    runapp(root)
    root.mainloop()