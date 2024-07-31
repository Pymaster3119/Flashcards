import tkinter
import main
import pickle
import random
root = tkinter.Tk()
outputvar = tkinter.StringVar(root)
userinput = tkinter.StringVar(root)
#REPLACE
setname = input("What set do you want?: ")
with open(setname, "rb") as txt:
    set = pickle.load(txt)
    print(set)

random.shuffle(set)
idx = 0
outputvar.set("What is meant by " + set[idx].term)
def check():
    global idx
    print(idx)
    try:
        if idx == -2:
            root.quit()
            return
        if userinput.get() == set[idx].definition:
            idx += 1
            outputvar.set("Correct! Now, what is meant by "+ set[idx].term)
            main.playSound("restartSession.mp3")
        else:
            outputvar.set("Incorrect. " + set[idx].term + " actually means " + set[idx].definition + ". Now, what is meant by " + set[idx + 1].term)
            idx += 1
    except IndexError:
        idx = -2
        outputvar.set('Set done! Now, just press the "Check" button to end the session.')
tkinter.Label(root, textvariable=outputvar).pack()
tkinter.Entry(root, textvariable=userinput).pack()
tkinter.Button(root, text="Check", command=check).pack()
root.mainloop()