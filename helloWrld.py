from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk

filename = "none"

def UploadAction(event=None):
    filename = filedialog.askopenfilename()
    print('Selected:', filename)
    PhotoImage.config(file=filename)
    fileNameTxt.config(text = filename)

root = Tk()
root.geometry("300x200")
root.title('Super AI gigabrain')


header = Label(root, text="Digit recogniser!")

button = Button(root, text='Open', command=UploadAction)

fileNameTxt = Label(root, text="File:" )
photo = PhotoImage(file='./file-icon.png')
image_label = ttk.Label(
    root,
    image=photo,
    text=filename,
    compound='top'
)

quitBtn = Button(root, text="Quit", command=root.destroy)

header.pack()
button.pack()
fileNameTxt.pack()
image_label.pack()
quitBtn.pack()

root.mainloop()