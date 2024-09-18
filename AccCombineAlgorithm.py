import math
import os
import pandas as pd


directory = '/Users/ansh/Downloads/S Nallamothu and C Culbertson 2023'

#Iteraters through particpants
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)

    #Iterates through different times
    if os.path.isdir(f):
        for filename2 in os.listdir(f):
            f2 = os.path.join(f, filename2)

            #Iterates through .csv files
            if os.path.isdir(f2):
                for file in os.listdir(f2):
                    f3 = os.path.join(f2, file)


                    if file == "ACC.csv" and filename2 == "1647705360_A00925" :
                        # Logic for Finding Vector Displacment

                        df = pd.read_csv(f3)
                        new_df = df.iloc[:1]
                        new_df = new_df.drop(columns = new_df.columns[1:3])

                        for index, row in df.iterrows():

                            if index != 0:
                                value1 = row[df.columns[0]]  # x value
                                value2 = row[df.columns[1]]  # y value
                                value3 = row[df.columns[2]]  # z value

                                vector_displacement_mag = math.sqrt(value1 ** 2 + value2 ** 2  + value3 ** 2)

                                new_df = pd.concat([new_df, pd.DataFrame([{df.columns[1] : vector_displacement_mag}])], ignore_index=True)


                        value = new_df[0, 1]
