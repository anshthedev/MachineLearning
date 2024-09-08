import matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model


df = pd.read_csv('/Users/ansh/Downloads/homeprices.csv')

#Need of 2D array for fit instead of df.area
new_df = df.drop('price',axis='columns')

plt.xlabel("Area (sq/ft)")
plt.ylabel("Price ($)")
plt.scatter(df.area, df.price, color = 'red', marker = "+")

reg = linear_model.LinearRegression()

#Traning the linear regression
reg.fit(new_df.values, df.price)

plt.plot(df.area, reg.predict(new_df.values))

#Slope of line best fits
print(reg.coef_)

#Y Intercept of line best fits
print(reg.intercept_)

print(reg.predict([[3300]]))
plt.show()
