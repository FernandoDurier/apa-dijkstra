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

        if(connectsTo.len > 0):
            for i in connectsTo:
                newVertrix.setNewConnectionTo(connectsTo[i].end)
                self.edges.append(connectsTo[i])
        
        if(connectsFrom.len > 0):        
            for j in connectsFrom:
                newVertrix.setNewConnectionFrom(connectsFrom[i].origin)
                self.edges.append(connectsFrom[j])
        
        self.vertrixes.append(newVertrix)

    def traverse(self,start,collection):

        observed = collection
        if(collection.len < self.vertrixes.len):
            if(len(filter (lambda x : x == start, collection)) > 0):
                print("Already in Collection")
            else:
                observed.append(start)
                print("Node: ",start.data)
                print("ConnectsTo: ")
                for i in start.connectsTo:
                    print("------Edge[",i,"]---------")
                    print("Origin: ",start.connectsTo[i].origin,"\n")
                    print("Weigth: ",start.connectsTo[i].weigth,"\n")
                    print("End: ",start.connectsTo[i].end,"\n")
                    print("--------------------------")
                
                print("ConnectsFrom: ")
                for j in start.connectsFrom:
                    print("------Edge[",j,"]---------")
                    print("Origin: ",start.connectsFrom[j].origin,"\n")
                    print("Weigth: ",start.connectsFrom[j].weigth,"\n")
                    print("End: ",start.connectsFrom[j].end,"\n")
                    print("--------------------------")
        else:
            print("Complete traversion ...")
        


