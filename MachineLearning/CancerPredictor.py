import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("/Users/ansh/PycharmProjects/LearningPython/MachineLearning/Datasets/cancerData.csv")

df.drop(["Unnamed: 32", "id"], axis=1,inplace=True)

df.diagnosis = [1 if value == 'M' else 0 for value in df.diagnosis]

print(df.head())