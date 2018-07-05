import sys
import ntpath
from .datGraphParser import *
from .steinlibparser import *
from .graphPathFinder import *

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
            
            common = p
            
            for i in range(2):#used to get the file level, and its parent folder level
                common = os.path.dirname(common)
            
            filename = os.path.relpath(p, common)

            print("Dataset: ", filename)

            if('test-set-1' in p):
                graph = dgp.graphDatParser(p, filename, False)
                graphs.append(graph)
            
            elif('test-set-2' in p):
                graph = dgp.graphDatParser(p, filename, False)
                graphs.append(graph)
            
            else:
                graph = slp.graphParser(p, filename, False)
                graphs.append(graph)
        
        return graphs
        
                