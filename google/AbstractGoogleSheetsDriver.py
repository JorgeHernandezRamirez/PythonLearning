from abc import ABCMeta, abstractmethod


class AbstractGoogleSheetsDrive(metaclass=ABCMeta):

    def __init__(self, credentials):
        self._credentials = credentials

    @abstractmethod
    def createSheet(self, docname):
        pass

    @abstractmethod
    def getRange(self, range):
        pass

    @abstractmethod
    def setRange(self, range, values):
        pass

    @abstractmethod
    def getSheets(self):
        pass
