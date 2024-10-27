import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error
import math

df = pd.read_csv('/Users/ansh/PycharmProjects/LearningPython/MachineLearning/Datasets/ecommerce.csv')

# steps to create linear regression model

# select your features and your output
X = df[['Time on App', 'Time on Website', 'Avg. Session Length', 'Length of Membership']]
y= df['Yearly Amount Spent']

# split the data to make it more effiecent to test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# create the model and fit it to the data
lm = LinearRegression()
lm.fit(X_train, y_train)

# higher the number, the more important it is to your model
cdf = pd.DataFrame(lm.coef_, X.columns, columns=['Coef'])

# look at predictions from the data
predictions = lm.predict(X_test)
sns.scatterplot(x=predictions, y=y_test)
plt.xlabel('Predictions')

# these are all different ways of finding error
print("MAE: ", mean_absolute_error(y_test, predictions))
print("MSE: ", mean_squared_error(y_test, predictions))
print("RMSE: ", math.sqrt(mean_squared_error(y_test, predictions)))

# these plots see if your model is bias to one side
residuals = y_test - predictions
sns.displot(residuals, bins=60)







# this is called the External Balance Assessment
# helps with understanding coorelation between numerical
# datasets.

# show single plot between x and y variables
# sns.jointplot(x = "Time on App", y = "Yearly Amount Spent", data = df)
# plt.show()

# shows all correlation between the data's features
# sns.pairplot(df, kind = 'scatter', plot_kws={'alpha':0.4})
# plt.show()

# sns.lmplot(x="Length of Membership", y="Yearly Amount Spent", data = df)
# plt.show()