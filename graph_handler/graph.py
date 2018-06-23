from edge import *
from vertrix import *

class Graph:
    def __init__(self,entry):
        self.entry = Vertrix(entry)
        self.vertrixes = [entry]
        self.edges = []

    def getEntry(self):
        return self.entry

    def getVertrixes(self):
        return self.vertrixes
    
    def getEdges(self):
        return self.edges

    ##
    # @description this function adds a new vertrix to the graph structure
    # @param {String/Number} data is the value of the vertrix
    # @param {Array<Edge>} connectsTo is an array of edges to which the vertrix is connected to 
    # @param {Array<Edge>} connectsFrom is an array of edges from which the vertrix connects from
    # # 
    def addNewVertrix(self,data,connectsTo=[],connectsFrom=[]):
        newVertrix = Vertrix(data)

        for i in connectsTo:
            newVertrix.setNewConnectionTo(i)
            self.edges.append(i)
               
        for j in connectsFrom:
            newVertrix.setNewConnectionFrom(j)
            self.edges.append(j)
        
        self.vertrixes.append(newVertrix)


    ## 
    # @description this function traverses the graph structure using recursion as algorithimic strategy
    # @param{Vertrix} start is the entrypoint of our graph traversion, and then will be next vertrix
    # @param{Array<Vertrix>} collection is the set of traversed vertrixes
    # #
    def traverse(self,start,collection):

        observed = collection
        
        if(start in collection):
            print("Already in Collection")
        else:
            observed.append(start)
            print("Node: ",start.getData())
            print("Connections: ")
            for i in start.getNexts():
                print("Edge:{[",i.getData().getOrigin().getData(),"]-(",i.getData().getWeigth(),")->[",i.getData().getEnd().getData(),"]}\n")
                print()
            print("--------------------------\n")

        if(len(start.getNexts())>0):
            self.traverse(start.getNexts()[0].getData().getEnd(),observed)
        else:
            print("Complete traversion ...\n")
        


