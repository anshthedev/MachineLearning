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
# returns a list of the start and end times of each pre-event slice of the data file
# return list format:
# [
#   [startTime1, endTime1],
#   [startTime2, endTime2],
#    etc.
# ]
def getPreEventStartEndTimes(file_df, timestamp, seconds):
    # create a list for times
    # iterate through the timestamp file
      # if (timestamp-seconds) is within the range of the file
          # add [timestamp - seconds, timestamp] to list
    # return list
    # this method should be no longer than these comments
    
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

# receive data file, timestamp file, and interval length in seconds
# returns a list of the start and end times of each post-event slice of the data file
# return list format:
# [
#   [startTime1, endTime1],
#   [startTime2, endTime2],
#    etc.
# ]
def getPostEventStartEndTimes(file_df, timestamp, seconds):
    # create a list for times
    # iterate through the timestamp file
      # if timestamp+seconds is within the range of the file
          # add [timestamp, timestamp + seconds, timestamp] to list
    # return list

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

# receives data file, timestamp file and interval length in seconds
# returns THREE lists: a list of pre-event [start,end] indices, a list of post-event [start,end] indices, and a list of non-event [start,end] indices
# each of the three lists has format:
# [
#   [startIndex1, endIndex1],
#   [startIndex2, endIndex2],
#    etc.
# ]
def getAllEventIndices(file_path, timestamp, seconds):

    # call getPreEventStartEndTimes, getPostEventStartEndTimes
    
    # create list for pre-event indices, list for post-event indices, list for non-event indices
    # iterate through data file
      # for each item in each event time files, see if it falls between this index and the next one.
      # if so, add this index in the proper place to the indices list
      # you should be able to take advantage of the fact that the end of the pre-event is the start of the post-event
      # and take advantage of the fact that the timestamps are in chronological order
      
      # as you iterate through the data file, create start,end indices for non-event sections. 
      # each of these sections is (seconds) long, starting at the beginning of the file or at the end of each post-event section
      # any non-event section that overlaps the start of a pre-event gets discarded
      # this part is hard - I'll help you more.
    
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


# receives data file, timestamp file and interval length in seconds
# then writes three new files containing pre-event data sections, post-event data sections, and non-event data sections.
def writeAllEventDataWindows(dataFile, timestampFile, seconds):
    # call getAllEventIndices and store results
    # use the native slice operator to create slices of the data file
    # write each slice in the proper shape to the appropriate file
    # return boolean success or failure


    




files = getFiles('tags.csv')

for file in files:
    if os.stat(file).st_size > 0:

        time_df = pd.read_csv(file)

        df = getAllEventIndices(file.strip("tags.csv")+"ACCMag.csv", time_df, 15)
        print(file)
        print(df)

        df.to_csv(file.strip('tags.csv') + 'FocusedAccIndex.csv', index=False)

