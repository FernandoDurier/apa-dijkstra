from graph import *
from vertrix import *
from edge import *

entry = Vertrix(0)
v1 = Vertrix(1)
v2 = Vertrix(2)
g1 = Graph(entry)

g1.addNewVertrix(v1,[],[entry])
g1.addNewVertrix(v2,[entry],[v1])

g1.traverse()