import pickle
import os
import numpy as np

class Datahandler:
    def __init__(self):
        self.__load_model()
    def predict_number(self, image):
        image = self.__resize_image(image)
        y_predict = self.model.predict(image)

        return y_predict
    
    def __load_model(self):
        model_pkl_file = os.getcwd() + "\\Mode\\NumberModel.p"  
        with open(model_pkl_file, 'rb') as file:  
            self.model = pickle.load(file)

    def __resize_image(image):
        # Scale images to the [0, 1] range
        image = image.astype("float32") / 255
        # Make sure images have shape (28, 28, 1)
        image = np.expand_dims(image, -1)
        return image
        
