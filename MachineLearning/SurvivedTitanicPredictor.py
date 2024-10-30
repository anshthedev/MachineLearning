import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

df = pd.read_csv('/Users/ansh/PycharmProjects/LearningPython/MachineLearning/Datasets/titanic_data.csv')

df.drop(["Name", "PassengerId", "Cabin", "Ticket"], axis=1,inplace=True)

df.Sex = [0 if value == 'male' else 1 for value in df.Sex]

df['Embarked'] = [0 if value == 'S' else 1 if value == 'Q' else 2 for value in df['Embarked']]

df.dropna(inplace=True)

y = df['Survived']
X = df.drop(['Survived'], axis=1)

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

lr = LogisticRegression()

lr.fit(X_train, y_train)

predictions = lr.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print(y_test, predictions, X_test)

print(accuracy)


