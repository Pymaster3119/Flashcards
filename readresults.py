from tkinter import *
import pickle
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  
NavigationToolbar2Tk) 
from loadflashcards import *

class PreaformanceRow():
    def __init__(self, list, root):
        frame = Frame(root)
        frame.pack()
        Label(frame, text="Definition to term?:" + str(list[0])).grid(row=0, column=0)
        Label(frame, text="Number Correct?:" + str(list[1])).grid(row=0, column=1)
        Label(frame, text="Number of Terms?:" + str(list[2])).grid(row=0, column=2)

def runanalysis(root):
    iteration = 0
    percentages = []
    while True:
        iteration += 1
        try:
            with open("detailedresults/" + setname.get() + "|" + str(iteration), "rb") as txt:
                print("HERE")
                list = pickle.load(txt)
                print("HERE")
                print("LIST" + str(list))
                print(type(list[0].term))
                print(type(termname.get()))
                print(termname.get())
                for i in list:
                    print(len(i.term.lower()))
                    print(len(termname.get().lower()))
                    if i.term.lower() in termname.get().lower() or termname.get().lower() in i.term.lower():
                        print("HERE 2")
                        percentages.append(i.state)
        except Exception as e:
            print(e)
            break
    print(percentages)
    #Plot learninggraph
    fig = Figure(figsize = (5, 5), dpi = 100)
    plot1 = fig.add_subplot(111)
    plot1.plot(percentages)
    canvas = FigureCanvasTkAgg(fig, master = root)
    canvas.draw()
    canvas.get_tk_widget().pack()
termname = None
def creategui(root):
    global setname, termname
    for child in root.winfo_children():
        child.destroy()
    iteration = 0
    percentages = []
    while True:
        iteration += 1
        try:
            with open("results/" + setname.get() + "|" + str(iteration), "rb") as txt:
                list = pickle.load(txt)
                PreaformanceRow(list, root)
                percentages.append(list[1])
                print("here")
        except:
            break
    #Plot learninggraph
    fig = Figure(figsize = (5, 5), dpi = 100)
    plot1 = fig.add_subplot(111)
    plot1.plot(percentages)
    canvas = FigureCanvasTkAgg(fig, master = root)
    canvas.draw()
    canvas.get_tk_widget().pack()

    #Plot learningpath per term
    termname = StringVar(root)
    Entry(root, textvariable=termname).pack()
    Button(root, text="Run Stats", command=lambda: runanalysis(root)).pack()
setname = None
def runapp(root):
    global setname
    setname = StringVar()
    with open("flashcardsnames", "r") as txt:
        sets = txt.read().split("\n")
        setname.set(sets[0]) 
    OptionMenu(root, setname, *sets).pack()
    Button(root,text="Find Stats", command=lambda:creategui(root)).pack()

if __name__ == "__main__":
    root = Tk()
    runapp(root)
    root.mainloop()