import os
import cv2
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.keras.layers import Conv2DTranspose, AveragePooling2D, Dense, Flatten, Dropout, Reshape
from tensorflow import keras

# Loading the MNIST data set with samples and splitting it
mnist = tf.keras.datasets.mnist
(X_train, y_train), (X_test, y_test) = mnist.load_data()

X_train = X_train.astype("float32") / 255
X_test = X_test.astype("float32") / 255
X_train = np.expand_dims(X_train, -1)
X_test = np.expand_dims(X_test, -1)

y_train = keras.utils.to_categorical(y_train, 10)
y_test = keras.utils.to_categorical(y_test, 10)

input_shape = (28, 28, 1)

model = keras.Sequential(
    [
        Reshape(input_shape),
        AveragePooling2D(pool_size=(2, 2)),
        Conv2DTranspose(64, kernel_size=(3,3), activation="relu"),
        Flatten(input_shape=input_shape),
        Dense(128, activation="relu"),
        Dropout(0.5),
        Dense(10, activation="softmax")
    ]
)

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

model.fit(X_train, y_train, epochs=3, batch_size=128, validation_split=0.1)

# Evaluate
val_loss, val_acc = model.evaluate(X_test, y_test)
print(val_loss)
print(val_acc)

# Save model
model.save('own_model.model')