from ordered_linked_list.ordered_linked_list import *
from logger.timer import *
from graph_handler.edge import *
from graph_handler.vertrix import *
from graph_handler.graph import *
from dijkstra.closest_path import *
from data_loader.data_loader import *

def main():

    dl = Data_Loader()

    set1 = dl.loadData('./data/case1.csv')
    set2 = dl.loadData('./data/case2.csv')
    set3 = dl.loadData('./data/case3.csv')
    set4 = dl.loadData('./data/case4.csv')

    g1 = Graph(Vertrix(int(set1[0][0])))
    g2 = Graph(Vertrix(int(set2[0][0])))
    g3 = Graph(Vertrix(int(set3[0][0])))
    g4 = Graph(Vertrix(int(set4[0][0])))

    for tup in set1:
        g1.addNewConnection(Vertrix(tup[0]),tup[2],Vertrix(tup[1]))
    for tup in set2:
        g2.addNewConnection(Vertrix(tup[0]),tup[2],Vertrix(tup[1]))
    for tup in set3:
        g3.addNewConnection(Vertrix(tup[0]),tup[2],Vertrix(tup[1]))
    for tup in set4:
        g4.addNewConnection(Vertrix(tup[0]),tup[2],Vertrix(tup[1]))
 
    chosenGraph = g3
    print("-----------------------------------------------------------------------------------------------------")
    print(" Adjacence List: ")
    grepresentation = chosenGraph.getRepresentation()
    for v in grepresentation:
        connections = grepresentation[v]['v'].getNexts()
        beautifulCon = []
        for c in connections:
            beauty = "["+str(c.getOrigin().getData())+","+str(c.getWeigth())+","+str(c.getEnd().getData())+"]"
            beautifulCon.append(beauty)
        print("  [",grepresentation[v]['v'].getData(),"] = ", beautifulCon)

    print(Dijkstra(chosenGraph.getRepresentation(),chosenGraph.getEntry(),None))
    

main()