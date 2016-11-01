import pandas
import sort
import csv
import random
import time
import numpy
from monitoredsortingalgorithm import MonitoredSortingAlgorithm
from sort import quickSort
from sort import mergeSort
from sort import insertionSort
from sort import selectionSort
from sort import bubbleSort


def outputDataSizeResults():
    numberOfSorts = 5
    dataSizes = [1, 10, 100, 1000, 2000, 5000, 7000, 10000]
    fieldnames = ["data_size", "average_sort_time"]
    with open("output/bubbleSort-TemperatureData-DataSize.csv", 'w', newline="\n") as bubbleSortDataSize:
        bubbleSortDataSizeWriter = csv.DictWriter(bubbleSortDataSize, delimiter=",", fieldnames=fieldnames)
        bubbleSortDataSizeWriter.writeheader()
        tempatureData = pandas.read_csv("weatherdata.cvs", sep="\n", delimiter="\s+", header=None)[3].tolist()
        tempatureDataSize = len(tempatureData)
        print("Bubble Sort")
        for dataSize in dataSizes:
            if (dataSize > len(tempatureData)):
                dataSize = len(tempatureData)
            print(dataSize)
            sortTimes = []
            for sortIndex in range(0, numberOfSorts):
                start = time.time()
                sort.bubbleSort(tempatureData[:dataSize])
                end = time.time()
                sortTimes.append(round((end - start)))
            averageSortTime = round(sum(sortTimes) / float(numberOfSorts), 4)
            bubbleSortDataSizeWriter.writerow({"data_size": dataSize, "average_sort_time": averageSortTime})



# function that makes a list a certain percentage sorted
def partialSort(inputList, percentageSorted):
    sortedList = inputList[:]
    sortedList.sort()
    sortToIndex = int(len(inputList) * (percentageSorted / 100))
    unsortedPart = sortedList[sortToIndex:]
    unsortedPart.reverse()
    for currentIndex in range(sortToIndex, len(inputList)):
        sortedList[currentIndex] = unsortedPart[currentIndex - sortToIndex]
    return sortedList


def main():
    # Anchorage & Fairbanks Daily Temperature data
    # 10,000 entries
    # source: http://academic.udayton.edu/kissock/http/Weather/gsod95-current/AKANCHOR.txt
    # and source: http://academic.udayton.edu/kissock/http/Weather/gsod95-current/AKFAIRBA.txt
    # tempatureData = pandas.read_csv("weatherdata.cvs", sep="\n", delimiter="\s+", header=None)[3].tolist()
    pass


if __name__ == "__main__":
    main()
