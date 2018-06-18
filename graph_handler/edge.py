class Edge:
    def __init__(self,origin,end,weigth=1):
        self.origin = origin
        self.end = end
        self.weigth = weigth

    def getOrigin(self):
        return self.origin

    def getEnd(self):
        return self.end
    
    def getWeigth(self):
        return self.weigth

    def setWeigth(self,newweigth):
        self.weigth = newweigth
    
    def setOrigin(self,newweigth):
        self.origin = neworigin

    def setEnd(self,newend):
        self.end = newend

