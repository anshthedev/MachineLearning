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

# create a list for times
# iterate through the timestamp file
  # if (timestamp-seconds) is within the range of the file
      # add [timestamp - seconds, timestamp] to list
# return list
# this method should be no longer than these comments
def getPreEventStartEndTimes(data_file, timestamp_file, seconds):

    list = []

    data_file = pd.read_csv(data_file)

    # this step is needed because when iterating it ignore the first row which is the header
    header = float(timestamp_file.columns[0])

    if data_file['TimeStamp'].iloc[0] - seconds < (header - seconds) < data_file['TimeStamp'].iloc[-1]:
        list.append([header - seconds, header])

    for timestamp in timestamp_file.iloc[:, 0]:
        if data_file['TimeStamp'].iloc[0] - seconds < (timestamp-seconds) < data_file['TimeStamp'].iloc[-1]:
            list.append([timestamp-seconds, timestamp])

    return list


# receive data file, timestamp file, and interval length in seconds
# returns a list of the start and end times of each post-event slice of the data file
# return list format:
# [
#   [startTime1, endTime1],
#   [startTime2, endTime2],
#    etc.
# ]
# create a list for times
# iterate through the timestamp file
  # if timestamp+seconds is within the range of the file
      # add [timestamp, timestamp + seconds, timestamp] to list
# return list
def getPostEventStartEndTimes(data_file, timestamp_file, seconds):
    list = []

    data_file = pd.read_csv(data_file)

    # this step is needed because when iterating it ignore the first row which is the header
    header = float(timestamp_file.columns[0])

    if data_file['TimeStamp'].iloc[0] + seconds < (header + seconds) < data_file['TimeStamp'].iloc[-1]:
        list.append([header, header+seconds])

    for timestamp in timestamp_file.iloc[:, 0]:
        if data_file['TimeStamp'].iloc[0] + seconds < (timestamp+seconds) < data_file['TimeStamp'].iloc[-1]:
            list.append([timestamp, timestamp+seconds])

    return list


# receives data file, timestamp file and interval length in seconds
# returns THREE lists: a list of pre-event [start,end] indices, a list of post-event [start,end] indices, and a list of non-event [start,end] indices
# each of the three lists has format:
# [
#   [startIndex1, endIndex1],
#   [startIndex2, endIndex2],
#    etc.
# ]
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
def getAllEventIndices(data_file, timestamp, seconds):

    # used to store the actual indices of each time
    pre_index_list = []
    post_index_list = []
    nonevent_index_list = []
    all_timestamp = []

    # used to store the index values
    startnon = 0
    endnon = 0
    start_index = 0
    mid_index = 0

    pre_list = getPreEventStartEndTimes(data_file, timestamp, seconds)
    post_list = getPostEventStartEndTimes(data_file, timestamp, seconds)

    # creates array that has all time stamp values neatly
    for i in range(len(pre_list)):
        all_timestamp.extend(pre_list[i])
        all_timestamp.append(post_list[i][1])

    data_file = pd.read_csv(data_file)

    # loop tracking
    data_index = 0
    i=0

    for data_value in data_file['TimeStamp']:
        data_index += 1
        if i < len(all_timestamp):
            if all_timestamp[i] <= data_value and i % 3 == 0:
                start_index = data_index-1
                endnon = data_index

                nonevent_index_list.append([startnon, endnon])
                i += 1

            elif all_timestamp[i] <= data_value and i % 3 == 1:
                mid_index = data_index
                i += 1


                pre_index_list.append([start_index, mid_index])

            elif all_timestamp[i] <= data_value and i % 3 == 2:
                post_index_list.append([mid_index, data_index])
                startnon = data_index - 1

                if(i == len(all_timestamp)-1):
                    nonevent_index_list.append([data_index, len(data_file)])

                i += 1

    print(f"Pre_Indices: {pre_index_list}")
    print(f"Post_Indices: {post_index_list}")
    print(f"Nonevent_Indices: {nonevent_index_list}")

    return pre_index_list, post_index_list, nonevent_index_list






# receives data file, timestamp file and interval length in seconds
# then writes three new files containing pre-event data sections, post-event data sections, and non-event data sections.
# def writeAllEventDataWindows(dataFile, timestampFile, seconds):
    # call getAllEventIndices and store results
    # use the native slice operator to create slices of the data file
    # write each slice in the proper shape to the appropriate file
    # return boolean success or failure





files = getFiles('tags.csv')

for file in files:
    if os.stat(file).st_size > 0:

        time_df = pd.read_csv(file)

        print(getPreEventStartEndTimes(file.strip("tags.csv")+"ACCMag.csv", time_df, 15))
        print(getPostEventStartEndTimes(file.strip("tags.csv")+"ACCMag.csv", time_df, 15))
        getAllEventIndices(file.strip("tags.csv")+"ACCMag.csv", time_df, 15)
        print(file.strip("tags.csv"))

        #just testing one iteration
        break