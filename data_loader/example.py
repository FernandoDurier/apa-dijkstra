# from steinlibparser import *
# from datGraphParser import *
# from graphPathFinder import *

# sp = steinlibParser()
# datp = datGraphParser()
# pathFinder = graphPathFinder()

# paths = pathFinder.exploreFolder('./data')
# print("Paths: ")
# for p in paths['files']:
#     print("File: ", p)

# graphAttempt1 = sp.graphParser("./data/ALUE/2015.dat", False)
# graphAttempt2 = datp.graphDatParser("./data/test-set-1/inst_v100_s1.dat", False)

# print("----------------------------------")
# print("Graph 1 Simplified:")
# print(graphAttempt1)
# print("----------------------------------")
# print("Graph 2 Simplified:")
# print(graphAttempt2)
# print("----------------------------------")

from data_loader import *

dl = Data_Loader()

graphSet = dl.loadData('./data')
print("GraphSet: ")
print(graphSet)
