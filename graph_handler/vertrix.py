import sys
sys.path.append('./')

from ordered_linked_list.ordered_linked_list import *
from graph_handler.edge import *

class Vertrix:
    def __init__(self,initdata):
        self.data = initdata
        self.connectsto = OrderedList()

    def getData(self):
        return self.data

    def getNexts(self):
        return self.connectsto.walk()

    def setData(self,newdata):
        self.data = newdata
    
    def getHead(self):
        return self.connectsto.getHead()

    ## 
    # @description This function adds a new edge to an ordered list of connected to edges 
    # @param {Edge} newnext is a new edge to which the vertrix is connected to
    # #
    def setNewConnectionTo(self,newnext):
        self.connectsto.add(newnext)