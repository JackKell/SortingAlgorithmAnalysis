import random
import time


# swaps two values within the inputlist at the two given indexes
def swap(inputList, index1, index2):
    inputList[index1], inputList[index2] = inputList[index2], inputList[index1]


# sorts a given list using the bubble sort algorithm
def bubbleSort(inputList):
    # Create a copy of the inputList so the original is not mutated
    sortedList = inputList[:]
    # for each index iterate through every index of the list
    for overallIndex in range(0, len(sortedList) - 1):
        for currentIndex in range(0, len(sortedList) - 1):
            currentItem = sortedList[currentIndex]
            nextItem = sortedList[currentIndex + 1]
            # check if the current item and the next are in the correct order
            if (currentItem > nextItem):
                # if not then swap the items
                sortedList[currentIndex] = nextItem
                sortedList[currentIndex + 1] = currentItem
    # Return a sorted version of the input list
    return sortedList

# sorts a given list using the merge sort algorithm
def mergeSort(inputList):
    # an internal function that merges two lists in sorted order
    def merge(leftList, rightList):
        # copy both lists
        leftList = leftList[:]
        rightList = rightList[:]
        mergedList = []
        # while their are still items within both copieds lists
        while(bool(leftList) and bool(rightList)):
            # check which list has the smallest value at the first index
            # if the left list is smaller than the right
            if(leftList[0] < rightList[0]):
                # add the first left item to the merged list
                mergedList.append(leftList[0])
                # and remove it from the left list
                leftList.pop(0)
            else:
                # add the first right item to the merged list
                mergedList.append(rightList[0])
                # and remove it from the right list
                rightList.pop(0)
        # add the remaining items from left list to merged list
        mergedList.extend(leftList)
        # add teh remaining items from right list to merged list
        mergedList.extend(rightList)

        return mergedList

    # Create a copy of the inputList so the original is not mutated
    sortedList = inputList[:]

    lengthOfList = len(sortedList)

    # if the list only has one item return the list
    if (lengthOfList == 1):
        return sortedList

    # split the input left into two parts at the middle index then merge sort them
    middle = lengthOfList // 2
    leftList = mergeSort(sortedList[:middle])
    rightList = mergeSort(sortedList[middle:])

    # merge both parts
    mergedList = merge(leftList, rightList)

    # return the merged and sorted list
    return mergedList


# sorts a given list using the merge sort algorithm
def selectionSort(inputList):
    # Create a copy of the inputList so the original is not mutated
    sortedList = inputList[:]
    lengthOfList = len(sortedList)
    # keep tract of where listed sorted up too
    for currentMinIndex in range(0, lengthOfList):
        # store the current the index the smallest value
        minValueIndex = currentMinIndex
        minValue = sortedList[minValueIndex]
        # iterate through the unsorted part of the list
        for currentIndex in range(currentMinIndex + 1, lengthOfList):
            # check if the current item is less than the current smallest value
            if (sortedList[currentIndex] < minValue):
                minValueIndex = currentIndex
                minValue = sortedList[minValueIndex]

        # swap the min value index with the current value index
        swap(sortedList, minValueIndex, currentMinIndex)
    # return the sorted list
    return sortedList


# sorts a given list using the insertion sort algorithm
def insertionSort(inputList):
    # Create a copy of the inputList so the original is not mutated
    sortedList = inputList[:]
    # Iterate through each index
    for currentIndex in range(0, len(sortedList) - 1):
        # Check if the current value and next value order
        currentValue = sortedList[currentIndex]
        nextValue = sortedList[currentIndex + 1]
        if (currentValue > nextValue):
            # if not then swap the current and next value
            swap(sortedList, currentIndex, currentIndex + 1)
            # if current index is not at the start of the list
            if (currentIndex > 0):
                # iterate back through the list and check if the value that was just switch is correct
                for backIndex in range(0, currentIndex):
                    # if the value that was just switched is less than the value before it
                    if (sortedList[currentIndex - backIndex] < sortedList[currentIndex - backIndex - 1]):
                        # then swap them
                        swap(sortedList, currentIndex - backIndex, currentIndex - backIndex - 1)
                    # else the rest of the list before the current is sorted so break the check loop
                    else:
                        break
    # return the sorted list
    return sortedList


# sorts a given list using the quick sort algorithm
def quickSort(inputList):
    # the internal function that recursively quick sorts the list
    def quickSortHelper(inputList, leftIndex, rightIndex):
        # if there is only one element in the list then return
        if (leftIndex >= rightIndex):
            return
        # set the low and high index values
        lowIndex = leftIndex
        highIndex = rightIndex
        # set the pivot value to a random indexed value within the input list
        pivot = inputList[random.randint(leftIndex, rightIndex)]

        # while the new pivot is not found
        while lowIndex <= highIndex:
            # if the low indexed value is less than the pivot
            while inputList[lowIndex] < pivot:
                # then move the low index right
                lowIndex += 1
            # if the high indexed value is greater than the pivot
            while inputList[highIndex] > pivot:
                # then move the high index left
                highIndex -= 1
            # if the low less than or equal to the high indexes
            if lowIndex <= highIndex:
                # then swap
                swap(inputList, highIndex, lowIndex)
                lowIndex += 1
                highIndex -= 1
        # quick sort the left partition
        quickSortHelper(inputList, leftIndex, highIndex)
        # quick sort the right partition
        quickSortHelper(inputList, lowIndex, rightIndex)

    # Create a copy of the inputList so the original is not mutated
    sortedList = inputList[:]
    # call the internal recursive quick sort helper function
    quickSortHelper(sortedList, 0, len(sortedList) - 1)
    # return the sorted list
    return sortedList


# determines if a given list is sorted or not
def isSorted(inputList):
    # iterate through the list and check if all the values are in order
    for currentIndex in range(0, len(inputList) - 1):
        # check value against the next value
        if (inputList[currentIndex] > inputList[currentIndex + 1]):
            # return False if out of order
            return False
    # return True if no check returned False
    # meaning the list is sorted (True)
    return True


def testSortingAlgorithms(inputList):
    print("Testing")
    print("List length: ", len(inputList))

    print("Bubble Sort")
    start = time.time()
    bubbleSorted = bubbleSort(inputList)
    end = time.time()
    print("Sorted: ", isSorted(bubbleSorted))
    print("Time (sec): ", str(end - start))

    print("Selection Sort")
    start = time.time()
    selectionSorted = selectionSort(inputList)
    end = time.time()
    print("Sorted: ", isSorted(selectionSorted))
    print("Time (sec): ", str(end - start))

    print("Merge Sort")
    start = time.time()
    mergeSorted = mergeSort(inputList)
    end = time.time()
    print("Sorted: ", isSorted(mergeSorted))
    print("Time (sec): ", str(end - start))

    print("Quick Sort")
    start = time.time()
    quickSorted = quickSort(inputList)
    end = time.time()
    print("Sorted: ", isSorted(quickSorted))
    print("Time (sec): ", str(end - start))

    print("Insertion Sort")
    start = time.time()
    insertionSorted = insertionSort(inputList)
    end = time.time()
    print("Sorted: ", isSorted(insertionSorted))
    print("Time (sec): ", str(end - start))
