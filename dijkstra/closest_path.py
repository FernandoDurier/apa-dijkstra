# Dijkstra's algorithm for shortest paths
# David Eppstein, UC Irvine, 4 April 2002

# http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/117228

from .priodict import priorityDictionary
from .heap import *

def Dijkstra(G,start,end=None):
    """
    Find shortest paths from the start vertex to all
    vertices nearer than or equal to the end.

    The input graph G is assumed to have the following
    representation: A vertex can be any object that can
    be used as an index into a dictionary.  G is a
    dictionary, indexed by vertices.  For any vertex v,
    G[v] is itself a dictionary, indexed by the neighbors
    of v.  For any edge v->w, G[v][w] is the length of
    the edge.  This is related to the representation in
    <http://www.python.org/doc/essays/graphs.html>
    where Guido van Rossum suggests representing graphs
    as dictionaries mapping vertices to lists of neighbors,
    however dictionaries of edges have many advantages
    over lists: they can store extra information (here,
    the lengths), they support fast existence tests,
    and they allow easy modification of the graph by edge
    insertion and removal.  Such modifications are not
    needed here but are important in other graph algorithms.
    Since dictionaries obey iterator protocol, a graph
    represented as described here could be handed without
    modification to an algorithm using Guido's representation.

    Of course, G and G[v] need not be Python dict objects;
    they can be any other object that obeys dict protocol,
    for instance a wrapper in which vertices are URLs
    and a call to G[v] loads the web page and finds its links.

    The output is a pair (D,P) where D[v] is the distance
    from start to v and P[v] is the predecessor of v along
    the shortest path from s to v.

    Dijkstra's algorithm is only guaranteed to work correctly
    when all edge lengths are positive. This code does not
    verify this property for all edges (only the edges seen
    before the end vertex is reached), but will correctly
    compute shortest paths even for some graphs with negative
    edges, and will raise an exception if it discovers that
    a negative edge has caused it to make a mistake.
    """
    #print("Graph: ", G)
    #print("\n \n \n")
    D = {}	# dictionary of final distances
    P = {}	# dictionary of predecessors
    Q = priorityDictionary()   # est.dist. of non-final vert.
    Q[int(start.getData())] = 0
    #print("------------------------------------Dijkstra-Execution----------------------------------------")
    #print("   Q(heapbin): ", Q)
    #print("   End(supposed): ", end)
    #print("   G: ", G)
    for vet in Q:
        #print("--------------------------------------------------------------------------------------------")
        #print("    Vet(next to be tested): ", vet)
        D[vet] = Q[vet]
        #if G[vet]['n'] == None:
            #print("Dead End ... ")
            #break
        if vet == end: 
            #print("End")
            break
        
        # for w in G[vet]['n']:
        #     #print("     W(edge): [",w.getOrigin().getData(),",",w.getWeigth(),",",w.getEnd().getData(),"]")
        #     vwLength = D[vet] + int(w.getWeigth())
        #     #print("     D(final distances): ", D)
        #     #print("     Q(heapbin): ", Q)
        #     if w.getEnd().getData() in D:
        #         if vwLength < D[w.getEnd.getData()]:
        #             raise str(ValueError) + " Dijkstra: found better path to already-final vertex"
        #     elif w.getEnd().getData() not in Q or vwLength < Q[w.getEnd().getData()]:
        #         Q[w.getEnd().getData()] = vwLength
        #         P[w.getEnd().getData()] = vet
        #     #print("     P(predecessors): ", P)
        #print("Vertrix: ", G[vet]['v'])
        link = G[vet]['v'].getHead()
        while link != None :
            #print("linked link: ", link)
            w = link.getData()
            #print("w: ", w)
            #print("     W(edge): [",w.getOrigin().getData(),",",w.getWeigth(),",",w.getEnd().getData(),"]")
            vwLength = D[vet] + int(w.getWeigth())
            #print("     D(final distances): ", D)
            #print("     Q(heapbin): ", Q)
            endOfEdge = w.getEnd()
            prioDictIndex = endOfEdge.getData()

            if prioDictIndex in D:
                if vwLength < D[prioDictIndex]:
                    raise str(ValueError) + " Dijkstra: found better path to already-final vertex"
                    
            elif prioDictIndex not in Q or vwLength < Q[prioDictIndex]:
                Q[prioDictIndex] = vwLength
                P[prioDictIndex] = vet
            
            if(link.getNext()):
                link = link.getNext()
            else:
                break
            #print("     P(predecessors): ", P)


    return {"distances":D,"predecessors":P}