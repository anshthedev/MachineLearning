from sklearn.metrics import mean_absolute_error, accuracy_score, mean_squared_error
import math

def accuracy(prediction, test):
    return accuracy_score(prediction, test)

def mae(prediction, test):
    return mean_absolute_error(prediction, test)

def mse(prediction, test):
    return mean_squared_error(prediction, test)

def rmse(prediction, test):
    return math.sqrt(mean_squared_error(test, prediction))