import sys
import csv
import operator

class Data_Loader:
    def __init__(self):
        pass

    def loadData(self,path):
        reader = csv.reader(open(path), delimiter=",")
        sortedlist = sorted(reader, key=operator.itemgetter(0), reverse=False)
        return sortedlist