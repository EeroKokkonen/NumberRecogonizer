from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk

filename = "none"

def UploadAction(event=None):
    filename = filedialog.askopenfilename()
    print('Selected:', filename)
    fileNameTxt.config(text = filename)

    loadedImg = Image.open(filename)
    resizedLoadedImg = loadedImg.resize((150,150))
    loadedImg = ImageTk.PhotoImage(resizedLoadedImg)
    imageBox.config(image=loadedImg)
    imageBox.image = loadedImg

root = Tk()
root.geometry("500x300")
root.title('Super AI gigabrain')


header = Label(root, text="Digit recogniser!")

button = Button(root, text='Open', command=UploadAction)

fileNameTxt = Label(root, text="File:" )

fileImage = Image.open("./UI/file-icon.png")
resizedFileImg = fileImage.resize((150, 150))
img = ImageTk.PhotoImage(resizedFileImg)
imageBox = Label(image=img)
imageBox.image = img

quitBtn = Button(root, text="Quit", command=root.destroy)

header.pack()
button.pack()
fileNameTxt.pack()
imageBox.pack()
quitBtn.pack()

root.mainloop()