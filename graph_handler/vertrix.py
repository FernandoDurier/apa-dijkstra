import sys
sys.path.append('./ordered_linked_list')

from ordered_linked_list import *

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

    def setNewConnectionTo(self,newnext):
        self.connectsto.add(newnext)
    
    def setNewConnectionFrom(self,newprevious):
        self.connectedfrom.add(newprevious)