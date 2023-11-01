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
root.geometry("500x300")
root.title('Super AI gigabrain')


header = Label(root, text="Digit recogniser!")

button = Button(root, text='Open', command=UploadAction)

fileNameTxt = Label(root, text="File:" )

image = Image.open("./UI/file-icon.png")
resize_image = image.resize((150, 150))
img = ImageTk.PhotoImage(resize_image)
label1 = Label(image=img)
label1.image = img


quitBtn = Button(root, text="Quit", command=root.destroy)

header.pack()
button.pack()
fileNameTxt.pack()
label1.pack()
quitBtn.pack()

root.mainloop()