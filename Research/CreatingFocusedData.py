import os
import pandas as pd
import numpy as np

# used one particpant as testcase due to GitHub sizing limit
directory = '/Users/ansh/PycharmProjects/LearningPython/Research/Particiapnt 1'

def getFiles(searchterm):
    filelist = []

    for dirpath, dirnames, filenames in os.walk(directory):  # gets all filenames in all subdirectories

        for f in filenames:

            if f.__contains__(searchterm):  # filter, then ...

                filelist = np.append(filelist, os.path.join(dirpath, f))  # create list of target files

    return filelist

def getPreEventStartEnd(file_df, timestamp, seconds):
    start = timestamp - seconds
    end = timestamp

    for time in file_df['TimeStamp']:
        if start <= time:
            start = time
            break

    for time in file_df['TimeStamp']:
        if end <= time:
            end = time
            break

    return file_df[file_df['TimeStamp'] == start].index[0], file_df[file_df['TimeStamp'] == end].index[0]

def getPostEventStartEnd(file_df, timestamp, seconds):

    start = timestamp

    for time in file_df['TimeStamp']:
        if start <= time:
            start = time
            end = start + seconds
            break

    for time in file_df['TimeStamp']:
        if end <= time:
            end = time
            break

    return file_df[file_df['TimeStamp'] == start].index[0], file_df[file_df['TimeStamp'] == end].index[0]

def getAllEventIndices(file_path, timestamp, seconds):
    combine_df = pd.DataFrame(columns=["StartPre", "EndPre", "StartPost", "EndPost"])

    file = pd.read_csv(file_path)

    column_timestamp = float(time_df.columns[0])

    pre_start, pre_end = getPreEventStartEnd(file, column_timestamp, seconds)
    post_start, post_end = getPostEventStartEnd(file, column_timestamp, seconds)

    # Creating a new row
    new_row = pd.DataFrame([[pre_start, pre_end, post_start, post_end]], columns=combine_df.columns)
    # Concatenate the new row with combine_df
    combine_df = pd.concat([combine_df, new_row], ignore_index=True)

    for timestamp in time_df.iloc[:, 0]:
        pre_start, pre_end = getPreEventStartEnd(file, timestamp, seconds)
        post_start, post_end = getPostEventStartEnd(file, timestamp, seconds)

        # Creating a new row
        new_row = pd.DataFrame([[pre_start, pre_end, post_start, post_end]], columns=combine_df.columns)
        # Concatenate the new row with combine_df
        combine_df = pd.concat([combine_df, new_row], ignore_index=True)

    return combine_df

files = getFiles('tags.csv')

for file in files:
    if os.stat(file).st_size > 0:

        time_df = pd.read_csv(file)

        df = getAllEventIndices(file.strip("tags.csv")+"ACCMag.csv", time_df, 15)
        print(file)
        print(df)

        df.to_csv(file.strip('tags.csv') + 'FocusedAccIndex.csv', index=False)
        # # testing one file
        # break






    #
    # print(time_df)
    # for time in time_df:
    #     print(time)
    #     # print(getAllEventIndices(file.strip('tag.csv') + 'ACCMag.csv', event, 15))
    #



# main
# files = getFiles('ACCMag.csv')
#
#
# for file in files:
    # df = pd.read_csv(file)
    #
    # for time in df['TimeStamp']:
    #     if event <= time:
    #         event = time
    #         end = event + 15
    #         break
    #
    # for time in df['TimeStamp']:
    #     if end <= time:
    #         end = time
    #         break
    #
    #
    # extract = df.iloc[df[df['TimeStamp'] == event].index[0]: df[df['TimeStamp'] == end].index[0] + 1]
    #
    # result = pd.DataFrame(extract, columns=['TimeStamp', 'AccMag'])
    # result.to_csv(file.strip('ACCMag.csv') + 'PostEventACC.csv', index=False)


# pre event
# for file in files:
#
    # df = pd.read_csv(file)
    #
    # end = event
    # event = event - 15
    #
    # for time in df['TimeStamp']:
    #     if event <= time:
    #         event = time
    #         break
    #
    # for time in df['TimeStamp']:
    #     if end <= time:
    #         end = time
    #         break
    #
    #
    # extract = df.iloc[df[df['TimeStamp'] == event].index[0]: df[df['TimeStamp'] == end].index[0] + 1]
    #
    # result = pd.DataFrame(extract, columns=['TimeStamp', 'AccMag'])
    # result.to_csv(file.strip('ACCMag.csv') + 'PreEventACC.csv', index=False)
    #


