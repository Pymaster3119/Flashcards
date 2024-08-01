from tkinter import *
import pickle
root = Tk()
class PreaformanceRow():
    def __init__(self, list, root):
        frame = Frame(root)
        frame.pack()
        Label(frame, text="Definition to term?:" + str(list[0])).grid(row=0, column=0)
        Label(frame, text="Number Correct?:" + str(list[1])).grid(row=1, column=0)
        Label(frame, text="Number of Terms?:" + str(list[2])).grid(row=2, column=0)

iteration = 0
#Replace
setname = input("Name of set?: ")
while True:
    iteration += 1
    try:
        with open("results/" + setname + "|" + str(iteration), "rb") as txt:
            PreaformanceRow(pickle.load(txt), root)
    except:
        break
root.mainloop()