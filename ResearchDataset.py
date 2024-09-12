import os
import pandas as pd


directory = '/Users/ansh/Downloads/S Nallamothu and C Culbertson 2023'

joined_data = pd.DataFrame()

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    print(filename)
    if os.path.isdir(f):
        for filename2 in os.listdir(f):
            f2 = os.path.join(f, filename2)

            print(filename2)

            if os.path.isdir(f2):
                for filename3 in os.listdir(f2):
                    f3 = os.path.join(f2, filename3)

                    print(filename3)

                    if filename3 == 'TEMP.csv':
                        temp = pd.read_csv(f3)
                        df1 = pd.DataFrame(temp)
                        # temp_data.columns = [f'{col}_{filename}' for col in temp_data.columns]
                        #
                        # # Reset the index to avoid index issues and concatenate horizontally
                        # temp_data = temp_data.reset_index(drop=True)
                        #

                        if joined_data.empty:
                            joined_data = df1
                        else:
                            joined_data = pd.concat([joined_data.reset_index(drop=True), df1.reset_index(drop=True)],
                                                    axis=1)


joined_data.to_csv(f+'/CombinedTemp.csv')

