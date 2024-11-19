import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("/Users/ansh/PycharmProjects/LearningPython/MachineLearning/Datasets/insurance_data.csv")

plt.scatter(df.age, df.bought_insurance, marker="+", color="blue")
plt.xlabel("Age")
plt.ylabel("Bought Insurance")
plt.show()

