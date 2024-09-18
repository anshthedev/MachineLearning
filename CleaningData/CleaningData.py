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

#Removes unwanted characters
df['Phone_Number'] = df['Phone_Number'].str.replace('[^a-zA-Z0-9]','', regex=True)

#Makes the column values into string
df['Phone_Number'] = df['Phone_Number'].apply(lambda x: str(x))

#Adds dashes using indexing of string method
df['Phone_Number'] = df['Phone_Number'].apply(lambda x: x[0:3] + '-' + x[3:6] + '-' + x[6:10])

#Removes blank phone numbers into empty
df['Phone_Number'] = df['Phone_Number'].str.replace('nan--', '', regex=True)
df['Phone_Number'] = df['Phone_Number'].str.replace('Na--', '', regex=True)
# df[["Street_Address", "State", "Zipcode"]] = df['Address'].str.split(',', 2, expand=True)

#Setting values to a common name
df["Paying Customer"] = df["Paying Customer"].str.replace("No", "N")
df["Paying Customer"] = df["Paying Customer"].str.replace("Yes", "Y")
df["Do_Not_Contact"] = df["Do_Not_Contact"].str.replace("No", "N")
df["Do_Not_Contact"] = df["Do_Not_Contact"].str.replace("Yes", "Y")

#Emptying out empty stuff
df = df.replace("N/a", "")
df = df.fillna('')

for x in df.index:
   if df.loc[x, "Do_Not_Contact"] == 'Y':
       df.drop(x, inplace=True)

df["Do_Not_Contact"] = df["Do_Not_Contact"].str.replace("N", "")
df["Do_Not_Contact"] = df["Do_Not_Contact"].str.replace("", "N")

#A way to remove empty rows
for x in df.index:
   if df.loc[x, "Phone_Number"] == '':
       df.drop(x, inplace=True)

#This is how you can reset the indexes of the table
df.reset_index(drop=True, inplace=True)




