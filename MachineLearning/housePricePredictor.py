import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error
import math

df = pd.read_csv("/Users/ansh/PycharmProjects/LearningPython/MachineLearning/Datasets/housePrices.csv")

sns.pairplot(df, kind = 'scatter', plot_kws={'alpha':0.1})
plt.show()
