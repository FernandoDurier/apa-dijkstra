from .edge import *
from .vertrix import *

class Graph:
    def __init__(self,entry,label):
        self.entry = Vertrix(entry)
        self.representation = {
            'label':label
        } #dictionary of ordered linked lists, adjacent row access complexity to O(1)*O(n) | n=size of each adjacence list

    def getEntry(self):
        return self.entry

    def getVertrixes(self):
        return self.representation.keys()
    
    def getEdges(self):
        edges = list()
        for k in self.representation.keys():
            edges.append(self.representation[int(k)]['v'].getNexts())
        return edges

    def addVertrix(self,vertrix):
        if vertrix.getData() in self.representation.keys():
            pass
        else: 
            self.representation[vertrix.getData()] = { 'v':vertrix , 'n':vertrix.getHead() }

    ##
    # @description this function adds a new vertrix to the graph structure
    # @param {String/Number} data is the value of the vertrix
    # @param {Array<Edge>} connectsTo is an array of edges to which the vertrix is connected to 
    # # 
    def addNewConnection(self,origin,distance,end):
        #print("edge to be added: [",origin.getData(),"]-(",distance,")->[",end.getData(),"]")
        newEdge = Edge(origin,end,distance)

        if origin not in self.representation.keys():
            self.addVertrix(origin)

        self.representation[origin.getData()]['v'].setNewConnectionTo(newEdge)
        self.representation[origin.getData()]['n'] = self.representation[origin.getData()]['v'].getNexts()
        
        if end not in self.representation.keys():
            self.addVertrix(end)
    
    def getRepresentation(self):
        return self.representation


        


