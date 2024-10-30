import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

from MachineLearning.CalculateError import accuracy

df = pd.read_csv("/Users/ansh/PycharmProjects/LearningPython/MachineLearning/Datasets/cancerData.csv")

df.drop(["Unnamed: 32", "id"], axis=1,inplace=True)

df.diagnosis = [1 if value == 'M' else 0 for value in df.diagnosis]

y = df['diagnosis']
X = df.drop(['diagnosis'], axis=1)

# Normalized values as close as possible to 0
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

lr = LogisticRegression()

lr.fit(X_train, y_train)

y_pred = lr.predict(X_test)

accuracy = accuracy(y_test, y_pred)

print(accuracy)

print(y_test)
print(y_pred)