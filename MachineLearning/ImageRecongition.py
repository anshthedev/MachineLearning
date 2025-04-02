# Fixes Certificate Errors
import ssl

from tensorflow.python.layers.core import flatten

ssl._create_default_https_context = ssl._create_unverified_context

# Import Dependencies and Libraries
import os
import random
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from keras import Sequential
from keras.src.layers import Dense, Conv2D, MaxPooling2D, Dropout, Flatten
from keras.src.datasets import cifar10
from keras.src.utils import to_categorical
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter)
from dataclasses import dataclass

# just to match the tutorial
SEED_VALUE = 42
random.seed(SEED_VALUE)
np.random.seed(SEED_VALUE)
tf.random.set_seed(SEED_VALUE)

# Loading Dataset
(X_train, y_train), (X_test, y_test) = cifar10.load_data()

# Normalizing Values
X_train = X_train.astype('float32')/255
X_test = X_test.astype('float32')/255

# One-Hot Encoding: converts harder to read outputs into binary vector matrix
# allowing computers to utilize information from categorical variable
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

# Classes to hold nescessary constants for later usuage
# (frozen=True) just means it can't be changed in the future
@dataclass(frozen=True)
class DatasetConfig:
    NUM_CLASSES: int = 10 # the number of possible outputs (airplanes, cars, ...)
    IMG_HEIGHT: int = 32
    IMG_WIDTH: int = 32
    NUM_CHANNELS: int = 3 # represents the three channels (Red, Green, Blue)

@dataclass(frozen=True)
class TrainingConfig:
    EPOCHS: int = 31 # number of times the model will go through the entire dataset
    BATCH_SIZE: int = 256 # amount pictures the model has to go through before changing features
    LEARNING_RATE: float = 0.001 # max amount the feature will change through iterations


def cnn_model(input_shape = (32, 32, 3)):

    # Allows us to add layers sequentially
    model = Sequential()

    # Padding = "Same" means the function will add some amount of rows and columns to the input such that
    # after doing the filtering, the output remains the same size as the input
    # 32 Different Filters with 3x3 Matrix are used

    # The reason we add two Conv2D layers in the same block is to allow the second layer to analyze and build on the
    # patterns detected by the first Conv2D. This helps extract more complex features before MaxPooling,
    # which reduces the loss of important details.

    #-------------------------------------------------
    # Conv Block 1: 32 Filters with Max Pooling
    #-------------------------------------------------

    model.add(Conv2D(filters=32, kernel_size=3, padding = "same", activation='relu', input_shape=input_shape))
    model.add(Conv2D(filters=32, kernel_size=3, padding = "same", activation='relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))

    #-------------------------------------------------
    # Conv Block 2: 64 Filters with Max Pooling
    #-------------------------------------------------
    model.add(Conv2D(filters=64, kernel_size=3, padding = "same", activation='relu'))
    model.add(Conv2D(filters=64, kernel_size=3, padding = "same", activation='relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))

    #-------------------------------------------------
    # Conv Block 3: 64 Filters with Max Pooling
    #-------------------------------------------------
    model.add(Conv2D(filters=64, kernel_size=3, padding = "same", activation='relu'))
    model.add(Conv2D(filters=64, kernel_size=3, padding = "same", activation='relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))

    #-------------------------------------------------
    # Flatten Features
    #-------------------------------------------------
    model.add(Flatten())
    model.add(Dense(512, activation='relu'))

    # Softmax helps convert the output array into probability array
    # Example:
    #
    # Input = (-1, 0, 3, 5)
    # Output = (0.002, 0.006, 0.118, 0.874)
    model.add(Dense(10, activation='softmax'))

    return model

model = cnn_model()
# print(model.summary())

#TODO: Understand this part
model.compile(
    optimizer='rmsprop',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

history = model.fit(
    X_train,
    y_train,
    batch_size=TrainingConfig.BATCH_SIZE,
    epochs=TrainingConfig.EPOCHS,
    verbose=1, # Helps monitor training by outputting basic updates
    validation_split=0.3
)