import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from CalculateError import *
data = load_breast_cancer()
dataset = pd.DataFrame(data=data.data, columns=data.feature_names)

X = dataset.copy()
y = data.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

clf = DecisionTreeClassifier()
clf = clf.fit(X_train, y_train)

predictions = clf.predict(X_test)

print(predictions)
print(accuracy(y_test, predictions))
