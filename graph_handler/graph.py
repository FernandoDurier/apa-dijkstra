from .edge import *
from .vertrix import *

class Graph:
    def __init__(self,entry,label,path):
        self.entry = Vertrix(entry)
        self.representation = {
            'label':label,
            'path':path,
            'struct':{}
        } #dictionary of ordered linked lists, adjacent row access complexity to O(1)*O(n) | n=size of each adjacence list

    def getEntry(self):
        return self.entry

    def getVertrixes(self):
        return self.representation['struct'].keys()
    
    def getEdges(self):
        edges = list()
        for k in self.representation['struct'].keys():
            edges.append(self.representation['struct'][k]['v'].getNexts())
        return edges
    
    def getQuantityOfEdges(self):
        size = 0
        for k in self.representation['struct'].keys():
            sizeK = self.representation['struct'][k]['v'].connectsto
            size += sizeK.size()
        return size

    def addVertrix(self,vertrix):
        if vertrix.getData() in self.representation['struct'].keys():
            pass
        else: 
            self.representation['struct'][vertrix.getData()] = { 'v':vertrix , 'n':vertrix.getHead() }

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

        if end not in self.representation['struct'].keys():
            self.addVertrix(end)
        
        self.representation['struct'][(origin.getData())]['v'].setNewConnectionTo(newEdge)
        #self.representation['struct'][(origin.getData())]['n'] = self.representation['struct'][(origin.getData())]['v'].getNexts()
    
    def getRepresentation(self):
        return self.representation


        


