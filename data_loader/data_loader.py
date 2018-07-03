import sys
from datGraphParser import *
from steinlibparser import *
from graphPathFinder import *

class Data_Loader:
    def __init__(self):
        pass

    def loadData(self, path):
        graphs = []
        gpf = graphPathFinder()
        dgp = datGraphParser()
        slp = steinlibParser()

        filesPaths = gpf.exploreFolder(path)['files']

        for p in filesPaths:
            print("P: ", p)
            if('test-set-1' in p):
                graph = dgp.graphDatParser(p,True)
                graphs.append(graph)
            
            elif('test-set-2' in p):
                graph = dgp.graphDatParser(p,False)
                graphs.append(graph)
            
            else:
                graph = slp.graphParser(p,False)
                graphs.append(graph)
        
        return graphs
        
                