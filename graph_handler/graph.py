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

    # This function adds a new vertrix and a new edge to the graph
    # data is the value of the new vertrix 
    # connectsTo is an array of edges that shows the connection between the new vertrix and outcoming ones
    # connectsFrom is an array of edges tht shows the connection between the new vertrix and incoming others

    def addNewVertrix(self,data,connectsTo=[],connectsFrom=[]):
        newVertrix = Vertrix(data)

        if(len(connectsTo) > 0):
            for i in connectsTo:
                newVertrix.setNewConnectionTo(i.end)
                self.edges.append(i)
        
        if(len(connectsFrom) > 0):        
            for j in connectsFrom:
                newVertrix.setNewConnectionFrom(j.origin)
                self.edges.append(j)
        
        self.vertrixes.append(newVertrix)

    def traverse(self,start,collection):

        observed = collection
        
        if(start in collection):
            print("Already in Collection")
        else:
            observed.append(start)
            print("Node: ",start.getData())
            print("ConnectsTo: ")
            for i in start.getNexts():
                print("------Edge[",i.getData().getOrigin().getData(),">",i.getData().getEnd().getData(),"]---------\n")
                print("Origin: ",i.getData().getOrigin().getData(),"\n")
                print("Weigth: ",i.getData().getWeigth(),"\n")
                print("End: ",i.getData().getEnd().getData(),"\n")
                print("--------------------------\n")
                
        if(len(start.getNexts())>0):
            self.traverse(start.getNexts()[0].getData().getEnd(),observed)
        else:
            print("Complete traversion ...\n")
        


