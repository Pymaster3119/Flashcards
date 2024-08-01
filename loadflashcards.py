import tkinter
import main
import pickle
import random

set = None
idx = 0
numcorrect = 0
def check(root):
    global idx, numcorrect
    if not swaptermsanddefinittions.get():
        try:
            print(set)
            if idx == -2:
                list = [swaptermsanddefinittions.get(), numcorrect, len(set)]
                iteration = 0
                while True:
                    iteration += 1
                    try:
                        open("results/" + setname.get() + "|" + str(iteration), "r").close()
                    except:
                        break
                with open("results/" + setname.get() + "|" + str(iteration), "wb") as txt:
                    pickle.dump(list,txt)
                root.quit()
                return
            if userinput.get() == set[idx].definition:
                idx += 1
                outputvar.set("Correct! Now, what is meant by "+ set[idx].term)
                main.playSound("restartSession.mp3")
                numcorrect += 1
            else:
                outputvar.set("Incorrect. " + set[idx].term + " actually means " + set[idx].definition + ". Now, what is meant by " + set[idx + 1].term)
                idx += 1
        except IndexError:
            idx = -2
            outputvar.set('Set done! Now, just press the "Check" button to end the session.')
    else:
        try:
            if idx == -2:
                list = [swaptermsanddefinittions.get(), numcorrect, len(set)]
                iteration = 0
                while True:
                    iteration += 1
                    try:
                        open("results/" + setname.get() + "|" + str(iteration), "r").close()
                    except:
                        break
                with open("results/" + setname.get() + "|" + str(iteration), "wb") as txt:
                    pickle.dump(list,txt)
                root.quit()
                return
            if userinput.get() == set[idx].definition: 
                idx += 1
                outputvar.set("Correct! Now, what has the definition "+ set[idx].definition)
                main.playSound("restartSession.mp3")
                numcorrect += 1
            else:
                outputvar.set("Incorrect. " + set[idx].definition + " actually belongs to " + set[idx].term + ". Now, what term has the definition " + set[idx + 1].definition)
                idx += 1
        except IndexError:
            idx = -2
            outputvar.set('Set done! Now, just press the "Check" button to end the session.')
def drawFirstSet(root):
    global set
    root.title("Review " + setname.get())
    with open(setname.get(), "rb") as txt:
        set = pickle.load(txt)
        print(set)
        random.shuffle(set)
    if not swaptermsanddefinittions.get():
        outputvar.set("What is meant by " + set[idx].term)
    else:
        outputvar.set("What term has the definition " + set[idx].definition)
    for child in root.winfo_children():
        child.destroy()

    tkinter.Label(root, textvariable=outputvar).pack()
    tkinter.Entry(root, textvariable=userinput).pack()
    tkinter.Button(root, text="Check", command=lambda:check(root)).pack()
    tkinter.Button(root, text="Home", command=lambda:main.render(root))


def runapp(root):
    global outputvar, userinput, setname, swaptermsanddefinittions
    outputvar = tkinter.StringVar()
    userinput = tkinter.StringVar()
    setname = tkinter.StringVar()
    swaptermsanddefinittions = tkinter.BooleanVar()
    with open("flashcardsnames", "r") as txt:
        sets = txt.read().split("\n")
        setname.set(sets[0])
    tkinter.OptionMenu(root, setname, *sets).pack()
    tkinter.Checkbutton(root, variable=swaptermsanddefinittions, text="Ask definition, recieve term").pack()
    tkinter.Button(root, text="Start!", command=lambda:drawFirstSet(root)).pack()
outputvar = None
userinput = None
setname = None
swaptermsanddefinittions = None

if __name__ == "__main__":
    root = tkinter.Tk()
    runapp(root)
    root.mainloop()