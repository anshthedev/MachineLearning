# Fixes Certificate Errors
import ssl
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
    EPOCHS: int = 10 # number of times the model will go through the entire dataset
    BATCH_SIZE: int = 256 # amount pictures the model has to go through before changing features
    LEARNING_RATE: float = 0.001 # max amount the feature will change through iterations

def plot_results(metrics, title=None, ylabel = None, ylim = None, metric_name = None, color = None):
    fig, ax = plt.subplots(figsize=(15, 4))

    if not (isinstance(metric_name, list) or isinstance(metric_name, tuple)):
        metrics = [metrics,]
        metric_name = [metric_name,]

    for idx, metric in enumerate(metrics):
        ax.plot(metric, color=color[idx])

    plt.xlabel("Epoch")
    plt.ylabel(ylabel)
    plt.title(title)
    plt.xlim(0, TrainingConfig.EPOCHS-1)
    plt.ylim(ylim)

    ax.xaxis.set_major_locator(MultipleLocator(5))
    ax.xaxis.set_major_formatter(FormatStrFormatter('%d'))
    ax.xaxis.set_minor_locator(MultipleLocator(1))
    plt.grid(True)
    plt.legend(metric_name)
    plt.show()
    plt.close()


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
    model.add(Dropout(0.25))

    #-------------------------------------------------
    # Conv Block 2: 64 Filters with Max Pooling
    #-------------------------------------------------
    model.add(Conv2D(filters=64, kernel_size=3, padding = "same", activation='relu'))
    model.add(Conv2D(filters=64, kernel_size=3, padding = "same", activation='relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    model.add(Dropout(0.25))

    #-------------------------------------------------
    # Conv Block 3: 64 Filters with Max Pooling
    #-------------------------------------------------
    model.add(Conv2D(filters=64, kernel_size=3, padding = "same", activation='relu'))
    model.add(Conv2D(filters=64, kernel_size=3, padding = "same", activation='relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    model.add(Dropout(0.25))

    #-------------------------------------------------
    # Flatten Features
    #-------------------------------------------------
    model.add(Flatten())
    model.add(Dense(512, activation='relu'))
    model.add(Dropout(0.5))

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
    validation_split=0.3 # keep 30% of dataset for validation purposes during training
)

train_acc = history.history['accuracy']
train_loss = history.history['loss']
val_acc = history.history['val_accuracy']
val_loss = history.history['val_loss']

plot_results([train_loss, val_loss],
             ylabel = "Loss",
             ylim = [0.0, 5.0],
             metric_name = ["Training Loss", "Validation Loss"],
             color = ["g", "b"])

plot_results([train_acc, val_acc],
             ylabel = "Accuracy",
             ylim = [0.0, 1.0],
             metric_name = ["Training Accuracy", "Validation Accuracy"],
             color = ["g", "b"])

# Testing the test case accuracy
test_loss, test_acc = model.evaluate(X_test, y_test)
print(f"Test Accuracy: {test_acc * 100 : 3f}")

# The Order is According to Dataset Documentation
class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer',
               'dog', 'frog', 'horse', 'ship', 'truck']

# Testing and Displaying First 10 Images with Outputs
for i in range(10):

  # Predicting
  pred = model.predict(X_test[i:i+1]) # using splice since model.predict expects a batch
  predicted_class = class_names[np.argmax(pred)]  # finds indice of largest value

  # Plot with label
  plt.imshow(X_test[i])
  plt.title(f"Predicted: {predicted_class}")
  plt.axis('off')
  plt.show()