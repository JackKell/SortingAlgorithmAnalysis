from threading import Thread
from threading import Event


class MonitoredSortingAlgorithm(Thread):
    def __init__(self, sortingAlgorithm, inputList):
        super(MonitoredSortingAlgorithm, self).__init__()
        self.sortingAlgorithm = sortingAlgorithm
        self.inputList = inputList
        self.monitor = Event()
        self.monitor.set()
        self.isShutdown = False

    def run(self):
        while self.isRunning():
            self.runSortingAlgorithm()
        self.isShutdown = True

    def stop(self):
        self.monitor.clear()

    def isRunning(self):
        return self.monitor.is_set()

    def runSortingAlgorithm(self):
        return self.sortingAlgorithm(self.inputList)
