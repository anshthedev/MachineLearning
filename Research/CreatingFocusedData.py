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

# recieve data file, timestamp file, and interval length in seconds
# returns a list of the start and end *indices* of each pre-event slice of the data file
# return list format:
# [
#   [startIndex1, endIndex1],
#   [startIndex2, endIndex2],
#    etc.
# ]
def getPreEventStartEnd(file_df, timestamp, seconds):
    # maybe break this out into helper method:
    # create a list for times
    # iterate through the timestamp file
      # add [timestamp - seconds, timestamp] to list
    # return list

    # create list of for indices
    # iterate through data file
      # for each item in the timestamp file, see if it falls between this index and the next one.
      # if so, add this index in the proper place to the indices list
    #return the indices list
    
    
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

