from graph import *
from vertrix import *
from edge import *

entry = Vertrix(0)
v1 = Vertrix(1)
v2 = Vertrix(2)
g1 = Graph(entry)
e1 = Edge(entry,v1,1)
e2 = Edge(v1,v2,1)
entry.setNewConnectionTo(e1)
v1.setNewConnectionTo(e2)
v1.setNewConnectionFrom(e1)
v2.setNewConnectionFrom(e2)

g1.addNewVertrix(v1,[],[e1])
g1.addNewVertrix(v2,[e2],[])

g1.traverse(entry,[])