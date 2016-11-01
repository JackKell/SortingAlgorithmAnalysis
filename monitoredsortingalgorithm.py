from threading import Thread
from threading import Event
from time import time


class MonitoredSortingAlgorithm(Thread):
    def __init__(self, sortingAlgorithm, inputList):
        super(MonitoredSortingAlgorithm, self).__init__()
        self.sortingAlgorithm = sortingAlgorithm
        self.inputList = inputList
        self.runTime = 0
        self.monitor = Event()
        self.monitor.set()
        self.isShutdown = False

    def run(self):
        start = time()
        while self.isRunning():
            self.runSortingAlgorithm()
            self.stop()
        end = time()
        self.runTime = end - start
        self.isShutdown = True

    def stop(self):
        self.monitor.clear()

    def isRunning(self):
        return self.monitor.is_set()

    def runSortingAlgorithm(self):
        return self.sortingAlgorithm(self.inputList)
