from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


def LinearRegressionModel(X, y, test_size):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)

    # create the model and fit it to the data
    lm = LinearRegression()
    lm.fit(X_train, y_train)

    return lm, X_test, y_test

