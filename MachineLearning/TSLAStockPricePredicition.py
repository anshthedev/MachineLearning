import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error
import math

df = pd.read_csv("/Users/ansh/PycharmProjects/LearningPython/MachineLearning/Datasets/tslaStockPrice.csv")

# sns.pairplot(df, kind = 'scatter', plot_kws={'alpha':0.4})
# plt.show()

X = df[['Open', 'Low', 'Adj Close', 'Close']]
y = df['High']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

lm = LinearRegression()

lm.fit(X_train, y_train)

predictions = lm.predict(X_test)
sns.scatterplot(x=predictions, y=y_test)
plt.xlabel("Predictions")
plt.title("Prediction vs High")

plt.show()

residuals = y_test - predictions
sns.displot(residuals, bins=20)
plt.show()