from ordered_linked_list.ordered_linked_list import *
from logger.timer import *
from graph_handler.edge import *
from graph_handler.vertrix import *
from graph_handler.graph import *
from dijkstra.closest_path import *
from data_loader.data_loader import *


def main():

    dl = Data_Loader()
    t = Timer()
    t2 = Timer()
    graphSet = dl.loadData('./data')

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
 
    graphs = [g1,g2,g3,g4]
    graphsLabels = ['g1','g2','g3','g4']
    for g in graphs:
        label = graphs.index(g)
        print("-----------------------------------------------------------------------------------------------------")
        print("Output graph: ", graphsLabels[label])
        chosenGraph = g
        t.set_timer_start()
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
        
        executionResult = {}
        for i in range(1000):
            print("#######################Execution Number ", i," #############################")
            executionResult = Dijkstra(chosenGraph.getRepresentation(),chosenGraph.getEntry(),None)
            print("###########################################################################")
        t.set_timer_end()
        print("------------------------------------------------------------")
        print("Dijkstra Result: ")
        print("distances set: ", executionResult['distances'])
        print("predecessors set: ", executionResult['predecessors'])
        print("------------------------------------------------------------")
        print("Time spent in miliseconds: ", t.get_timer_difference())
print("----------------------------------------------------------------------")
main()