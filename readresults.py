from tkinter import *
import pickle
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  
NavigationToolbar2Tk) 

class PreaformanceRow():
    def __init__(self, list, root):
        frame = Frame(root)
        frame.pack()
        Label(frame, text="Definition to term?:" + str(list[0])).grid(row=0, column=0)
        Label(frame, text="Number Correct?:" + str(list[1])).grid(row=0, column=1)
        Label(frame, text="Number of Terms?:" + str(list[2])).grid(row=0, column=2)

def creategui(root):
    global setname
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
    #Plot manefesto
    fig = Figure(figsize = (5, 5), dpi = 100)
    plot1 = fig.add_subplot(111)
    plot1.plot(percentages)
    canvas = FigureCanvasTkAgg(fig, master = root)
    canvas.draw()
    canvas.get_tk_widget().pack()
    toolbar = NavigationToolbar2Tk(canvas, root)
    toolbar.update()
    canvas.get_tk_widget().pack()
    print("hi")
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