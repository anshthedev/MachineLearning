import pandas as pd

df = pd.read_excel(r"/Users/ansh/Downloads/Customer Call List.xlsx")

#removes duplicates from dataframe
df = df.drop_duplicates()

#removes unneeded columns

df = df.drop(columns="Not_Useful_Column")

#methods of cleaning unwanted charcters:

# df['Last_Name'] = df['Last_Name'].str.lstrip("...")
# df['Last_Name'] = df['Last_Name'].str.lstrip("/")
# df['Last_Name'] = df['Last_Name'].str.rstrip("_")

#fastest way:

df['Last_Name'] = df['Last_Name'].str.strip("._/")





print(df)



