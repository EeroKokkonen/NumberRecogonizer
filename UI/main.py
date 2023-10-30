from tkinter import *
from tkinter import ttk
from tkinter import filedialog

filename = "none"

def UploadAction(event=None):
    filename = filedialog.askopenfilename()
    print('Selected:', filename)
    fileNameTxt.config(text = filename)

root = Tk()
root.geometry("300x200")

header = Label(root, text="Digit recogniser!")

button = Button(root, text='Open', command=UploadAction)

fileNameTxt = Label(root, text="File:" )

quitBtn = Button(root, text="Quit", command=root.destroy)

header.pack()
button.pack()
fileNameTxt.pack()
quitBtn.pack()

root.mainloop()