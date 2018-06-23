import sys
sys.path.append('./')

from ordered_linked_list import *
from graph_handler.edge import *

class Vertrix:
    def __init__(self,initdata):
        self.data = initdata
        self.connectsto = OrderedList()
        self.connectedfrom = OrderedList()

    def getData(self):
        return self.data

    def getNexts(self):
        return self.connectsto.walk()
    
    def getPrevious(self):
        return self.connectedfrom.walk()

    def setData(self,newdata):
        self.data = newdata

    ## 
    # @description This function adds a new edge to an ordered list of connected to edges 
    # @param {Edge} newnext is a new edge to which the vertrix is connected to
    # #
    def setNewConnectionTo(self,newnext):
        self.connectsto.add(newnext)
    
    # #
    # @description This function adds a new edge to an ordered list of connected from edges 
    # @parma {Edge} newprevious is a new edge to which the vertrix is connected from 
    # #
    def setNewConnectionFrom(self,newprevious):
        self.connectedfrom.add(newprevious)