import math
import os
import pandas as pd
import numpy as np


directory = '/Users/ansh/Downloads/S Nallamothu and C Culbertson 2023'


def getFiles(searchterm):
    filelist = []

    for dirpath, dirnames, filenames in os.walk(directory):  # gets all filenames in all subdirectories

        for f in filenames:

            if f.__contains__(searchterm):  # filter, then ...

                filelist = np.append(filelist, os.path.join(dirpath, f))  # create list of target files

    return filelist



def extractHeadersAndData(filename, numHeaderRows):
    fullArray = np.loadtxt(filename, delimiter=',')

    headers = fullArray[:numHeaderRows]  # use slice operator to extract rows

    data = fullArray[numHeaderRows:]

    headers = np.append(headers, (len(data)))  # add extra header row holding number of data rows

    return headers, data  # return tuple of header rows and data rows


def calcMagnitudes(xyzArray):
    magnitudes = []  # remove time header rows

    for row in range(len(xyzArray)):
        mag =  math.sqrt(xyzArray[row][0] ** 2 + xyzArray[row][1] ** 2 + xyzArray[row][2] ** 2)

        magnitudes.append(mag)

    return magnitudes


def makeTimestamps(headerRows):

    starttime = headerRows[0]

    frequency = headerRows[1]

    numSamples = headerRows[2]

    endtime = starttime + numSamples / frequency

    timestamps = np.arange(starttime, endtime, 1 / frequency)

    return timestamps


# main

files = getFiles('ACC.csv')

for file in files:
    headers, data = extractHeadersAndData(file, 2)

    times = makeTimestamps(headers)

    mags = calcMagnitudes(data)

print(mags)



    # figure out how to stack these two vectors (1d arrays) into a 2d array with each row being [time, magnitude]