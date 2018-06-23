[Back to Home](./)
# This is the Graph Manager Module of the Project

* Each vertrix in its topology has an ordered adjacence list of connections to and from other edges that will eventually connecto to other vertrixes. 

* The Vertrixes have the following structure:
1. Data: The value of the vertrix per say, normally an integer, but can be a string as well
2. connectsto: A set of edges to which this node connects to.
3. connectsfrom: A set of edges from which this node is connected from.

* The Edges have the following structure:
1. Origin: Pointer to the previous vertrix of the tuple
2. Weigth: Integer value that represent the edge weigth (what shall be used later on dijkstra algorithm)
3. End: Pointer to the next vertrix of the tuple

* The linked lists have nodes that have the following structure:
1. Data: The value of each node, in our case a pointer to an edge
2. Next: A list of ordered by weigth edges, e.g. 1 connects to 2 by three different edges being: e1,e2 and e3 those having respectively the weigths 3,2 and 1. So when we traverse the graph they should appear in the following order e3,e2 and e1.

* If you want to test an example of the traversion:
* Disclaimer: Python 3.6.7 was used during this project.
1. Issue the following command from the root of this project -> `python .\graph_handler\example.py`


