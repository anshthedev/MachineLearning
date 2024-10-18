import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

melbourne_data = pd.read_csv("/Users/ansh/PycharmProjects/LearningPython/MachineLearning/melb_data.csv")

features = ["Rooms", "Bathroom", "Landsize", "Lattitude","Longtitude"]

melbourne_data = melbourne_data.dropna(axis = 0)

y = melbourne_data.Price

x = melbourne_data[features]

# goal behind this is that we don't use the training data to be used as finding
# accuracy of the model. We use a different untrained data to actually see
# how well the model preforms for general usage
train_x, val_x, train_y, val_y = train_test_split(x, y, random_state = 0)

melbourne_model = DecisionTreeRegressor(random_state = 1)


def get_mae_tree(max_leaf_nodes, train_x, train_y, val_x, val_y):
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
    model.fit(train_x, train_y)

    return mean_absolute_error(val_y, model.predict(val_x))

def get_mae_forest(train_x, train_y, val_x, val_y):
    model = RandomForestRegressor(random_state = 1)
    model.fit(train_x, train_y)

    return mean_absolute_error(val_y, model.predict(val_x))

for max_leaf_nodes in [800]:
    mae = get_mae_tree(max_leaf_nodes, train_x, train_y, val_x, val_y)
    print((max_leaf_nodes, mae))
    print(get_mae_forest(train_x, train_y, val_x, val_y))


