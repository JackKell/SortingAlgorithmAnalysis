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
import resource
import statistics
from memory_profiler import memory_usage
from memory_profiler import profile
import psutil
import os


def outputDataSizeResult(sortingAlgorithms, dataSizes, inputList, outputfileName, numberOfSorts):
    fieldnames = ["sort", "data_size", "average_sort_time", "stdev_time", "average_memory_usage", "stdev_memory_usage"]
    with open(outputfileName, 'w', newline="\n") as outputfile:
        outputfilewriter = csv.DictWriter(outputfile, delimiter=",", fieldnames=fieldnames)
        outputfilewriter.writeheader()
        print(outputfileName)
        for sortingAlgorithm in sortingAlgorithms:
            for dataSize in dataSizes:
                inputListDataSize = inputList[:dataSize]
                print(dataSize)
                sortTimes = []
                memoryUsages = []

                for sortIndex in range(0, numberOfSorts):
                    start = time.time()
                    sortingAlgorithm(inputListDataSize)
                    end = time.time()
                    sortTimes.append((end - start))

                    memoryUsages.append(getMemoryUsage(sortingAlgorithm, inputListDataSize))

                averageSortTime = round(sum(sortTimes) / float(numberOfSorts), 6)
                averageMemoryUsage = round(sum(memoryUsages) / float(numberOfSorts), 6)
                stdevTime = round(statistics.stdev(sortTimes), 6)
                stdevMemoryUsage = round(statistics.stdev(memoryUsages), 6)

                outputfilewriter.writerow({"sort": sortingAlgorithm.__name__,
                                           "data_size": dataSize,
                                           "average_sort_time": averageSortTime,
                                           "stdev_time": stdevTime,
                                           "average_memory_usage": averageMemoryUsage,
                                           "stdev_memory_usage": stdevMemoryUsage})


def outputDataSortResult(sortingAlgorithms, dataSortednessValues, inputList,  outputfileName, numberOfSorts):
    fieldnames = ["sort", "data_sortedness", "average_sort_time", "stdev_time", "average_memory_usage", "stdev_memory_usage"]
    with open(outputfileName, 'w', newline="\n") as outputfile:
        outputfilewriter = csv.DictWriter(outputfile, delimiter=",", fieldnames=fieldnames)
        outputfilewriter.writeheader()
        print(outputfileName)
        for sortingAlgorithm in sortingAlgorithms:
            for dataSortednessValue in dataSortednessValues:
                inputListDataSize = partialSort(inputList, dataSortednessValue)
                print(dataSortednessValue)
                sortTimes = []
                memoryUsages = []

                for sortIndex in range(0, numberOfSorts):
                    start = time.time()
                    sortingAlgorithm(inputListDataSize)
                    end = time.time()
                    sortTimes.append((end - start))

                    memoryUsages.append(getMemoryUsage(sortingAlgorithm, inputListDataSize))

                averageSortTime = round(sum(sortTimes) / float(numberOfSorts), 6)
                averageMemoryUsage = round(sum(memoryUsages) / float(numberOfSorts), 6)
                stdevTime = round(statistics.stdev(sortTimes), 6)
                stdevMemoryUsage = round(statistics.stdev(memoryUsages), 6)

                outputfilewriter.writerow({"sort": sortingAlgorithm.__name__,
                                           "data_sortedness": dataSortednessValue,
                                           "average_sort_time": averageSortTime,
                                           "stdev_time": stdevTime,
                                           "average_memory_usage": averageMemoryUsage,
                                           "stdev_memory_usage": stdevMemoryUsage})


def outputDataSortResults():
    randomData = pandas.read_csv("data/randomdata.csv", sep="\n", delimiter=",", header=None)[0].tolist()
    roomCO2Data = pandas.read_csv("data/roomdata.csv", sep="\n", delimiter=",", header=None)[5].tolist()
    syntheticDiceData = pandas.read_csv("data/syntheticdicedata.csv", sep="\n", delimiter=",", header=None)[0].tolist()
    tempatureData = pandas.read_csv("data/weatherdata.cvs", sep="\n", delimiter="\s+", header=None)[3].tolist()

    numberOfSorts = 5
    dataSortednessValues = [25, 50, 75, 100]

    sortingAlgorithms = [quickSort, mergeSort, selectionSort, insertionSort, bubbleSort]

    outputDataSortResult(sortingAlgorithms, dataSortednessValues, randomData, "randomData-dataSort.csv", numberOfSorts)
    outputDataSortResult(sortingAlgorithms, dataSortednessValues, roomCO2Data, "roomCO2Data-dataSort.csv", numberOfSorts)
    outputDataSortResult(sortingAlgorithms, dataSortednessValues, syntheticDiceData, "syntheticDiceData-dataSort.csv", numberOfSorts)
    outputDataSortResult(sortingAlgorithms, dataSortednessValues, tempatureData, "tempatureData-dataSort.csv", numberOfSorts)

def outputDataSizeResults():
    randomData = pandas.read_csv("data/randomdata.csv", sep="\n", delimiter=",", header=None)[0].tolist()
    roomCO2Data = pandas.read_csv("data/roomdata.csv", sep="\n", delimiter=",", header=None)[5].tolist()
    syntheticDiceData = pandas.read_csv("data/syntheticdicedata.csv", sep="\n", delimiter=",", header=None)[0].tolist()
    tempatureData = pandas.read_csv("data/weatherdata.cvs", sep="\n", delimiter="\s+", header=None)[3].tolist()

    numberOfSorts = 5
    dataSizes = [1, 10, 100, 1000, 2000, 5000, 7000, 10000]
    sortingAlgorithms = [quickSort, mergeSort, selectionSort, insertionSort, bubbleSort]

    outputDataSizeResult(sortingAlgorithms, dataSizes, randomData, "randomData-dataSize.csv", numberOfSorts)
    outputDataSizeResult(sortingAlgorithms, dataSizes, roomCO2Data, "roomCO2Data-dataSize.csv", numberOfSorts)
    outputDataSizeResult(sortingAlgorithms, dataSizes, syntheticDiceData, "syntheticDiceData-dataSize.csv", numberOfSorts)
    outputDataSizeResult(sortingAlgorithms, dataSizes, tempatureData, "tempatureData-dataSize.csv", numberOfSorts)



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


def getCurrentMemoryUsage():
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss


def getBaseMemory():
    def memoryHelper():
        return
    baseMemoryUsages = memory_usage(memoryHelper, interval=0.00001)
    baseMemory = min(baseMemoryUsages)
    return baseMemory


def getMemoryUsage(sortingAlgorithm, inputList):
    memoryUsage = memory_usage((sortingAlgorithm, (inputList,), ), interval=0.001)
    # print(memoryUsage)
    return max(memoryUsage) - min(memoryUsage)

def temp():
    process = psutil.Process(os.getpid())
    mem = process.get_memory_info()[0] / float(2 ** 20)
    return mem

def main():
    # Anchorage & Fairbanks Daily Temperature data
    # 10,000 entries
    # source: http://academic.udayton.edu/kissock/http/Weather/gsod95-current/AKANCHOR.txt
    # and source: http://academic.udayton.edu/kissock/http/Weather/gsod95-current/AKFAIRBA.txt
    # tempatureData = pandas.read_csv("data/weatherdata.cvs", sep="\n", delimiter="\s+", header=None)[3].tolist()

    # inputList = [1, 2, 3, 6, 7, 8, 10]
    # print("Quick Sort")
    # print(getMemoryUsage(quickSort, tempatureData), " MB")
    # print("Merge Sort")
    # print(getMemoryUsage(mergeSort, tempatureData), " MB")
    # print("Insertion Sort")
    # print(getMemoryUsage(insertionSort, tempatureData), " MB")
    # print("Selection Sort")
    # print(getMemoryUsage(selectionSort, tempatureData), " MB")
    # print("Bubble Sort")
    # print(getMemoryUsage(bubbleSort, tempatureData), " MB")
    # bubble 0.08984375 MB

    outputDataSortResults()
    outputDataSizeResults()


if __name__ == "__main__":
    main()
