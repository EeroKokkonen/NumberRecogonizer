from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
import os
import numpy as np
import tensorflow as tf
import cv2

filename = "none"

class Datahandler:
    def __init__(self):
        self.__load_model()

    def predict_number(self, path):
        img = cv2.imread(path)[:,:,0]
        img = np.invert(np.array([img]))
        y_predict = self.model.predict(img)

        return y_predict
    
    def __load_model(self):
        self.model = tf.keras.models.load_model('handwritten_digits.model')

    def __resize_image(self, image):
        img = np.invert(np.array([image]))
        return img
        
def UploadAction(event=None):
    filename = filedialog.askopenfilename()
    print('Selected:', filename)
    fileNameTxt.config(text = filename)

    loadedImg = Image.open(filename)
    resizedLoadedImg = loadedImg.resize((150,150))
    loadedImg = ImageTk.PhotoImage(resizedLoadedImg)
    imageBox.config(image=loadedImg)
    imageBox.image = loadedImg
    datahandler = Datahandler()
    result = datahandler.predict_number(filename)
    print("The number is probably a {}".format(np.argmax(result)))



root = Tk()
root.geometry("500x300")
root.title('Super AI gigabrain')


header = Label(root, text="Digit recogniser!")

button = Button(root, text='Load Image', command=UploadAction)

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