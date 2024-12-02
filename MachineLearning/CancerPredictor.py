import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("/Users/ansh/PycharmProjects/LearningPython/MachineLearning/Datasets/cancerData.csv")
df.drop(["Unnamed: 32", "id"], axis=1, inplace=True)
df.diagnosis = [1 if value == 'M' else 0 for value in df.diagnosis]

X = df[['radius_mean']]
y = df['diagnosis']

# option to scale the numbers if using multiple features
# scaler = StandardScaler()
# X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

lr = LogisticRegression()
lr.fit(X_train, y_train)


y_pred = lr.predict(X_test)

# just so we can see the actual data
plt.scatter(X_test, y_test, color='blue', label='Actual Data')

# creates more points to use for the plot
x_range = np.linspace(X_test.min(), X_test.max(), 500)

# had to create this because the column name got lost after doing ranges
x_range_df = pd.DataFrame(x_range, columns=['radius_mean'])

# lr.predict-proba will create 2D array showing probability for each classifcation
# to actually plot it all we need is the probability that it is 1 so we just grab
# the last column (we are not finding the output but rather the probability)
y_probs = lr.predict_proba(x_range_df)[:, 1]
plt.plot(x_range, y_probs, color='red', label='Logistic Curve')

# adding labels to the graph
plt.xlabel('Radius Mean')
plt.ylabel('Diagnosis Probability')
plt.title('Logistic Regression Curve')
plt.legend()
plt.show()

