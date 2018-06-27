from graph import *
from vertrix import *
from edge import *

entry = Vertrix(0)
v1 = Vertrix(1)
v2 = Vertrix(2)

g1 = Graph(entry)

g1.addNewConnection(entry,1,v1)
g1.addNewConnection(v1,1,v2)
g1.addNewConnection(v1,2,v2)
g1.addNewConnection(v1,3,v2)

print("Adjacence List: ")
for v in g1.getVertrixes():
    connections = v.getNexts()
    beautifulCon = []
    for c in connections:
        beauty = "["+str(c.getOrigin().getData())+","+str(c.getWeigth())+","+str(c.getEnd().getData())+"]->"
        beautifulCon.append(beauty)
    print("[",v.getData(),"] = ", beautifulCon)

#g1.traverse(entry,[])