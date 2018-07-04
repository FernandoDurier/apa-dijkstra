from ordered_linked_list.ordered_linked_list import *
from logger.timer import *
from graph_handler.edge import *
from graph_handler.vertrix import *
from graph_handler.graph import *
from dijkstra.closest_path import *
from data_loader.data_loader import *
import json
import ntpath

def main():

    graphs = []
    dl = Data_Loader()
    t = Timer()
    t2 = Timer()
    graphSet = dl.loadData('./data')

    for i in graphSet:
        g = Graph(Vertrix(i['entry']),i['path'])
        for tup in i['edges']:
            g.addNewConnection(Vertrix(tup['origin']),tup['weigth'],Vertrix(tup['end']))
        graphs.append(g)
    
    for g in graphs:
        print("-----------------------------------------------------------------------------------------------------")
        chosenGraph = g
        t.set_timer_start()
        #print("-----------------------------------------------------------------------------------------------------")
        #print(" Adjacence List: ")
        # grepresentation = chosenGraph.getRepresentation()
        # for v in grepresentation:
        #     connections = grepresentation[v]['v'].getNexts()
        #     beautifulCon = []
        #     for c in connections:
        #         beauty = "["+str(c.getOrigin().getData())+","+str(c.getWeigth())+","+str(c.getEnd().getData())+"]"
        #         beautifulCon.append(beauty)
        #     print("  [",grepresentation[v]['v'].getData(),"] = ", beautifulCon)
        
        executionResult = {}
        executionResult = Dijkstra(chosenGraph.getRepresentation(),chosenGraph.getEntry(),None)
        t.set_timer_end()
        # print("------------------------------------------------------------")
        # print("Dijkstra Result: ")
        # print("Graph Analysed: ", chosenGraph['label'])
        # print("Number of Nodes: ", len(chosenGraph.getEdges()))
        # print("Number of Edges: ", len(chosenGraph.getVertrixes()))
        # print("Time spent in miliseconds: ", t.get_timer_difference())
        # print("distances set: ", executionResult['distances'])
        # print("predecessors set: ", executionResult['predecessors'])
        report = {}
        report["strategy"] = "binheap priority queue"
        report["instance"] = chosenGraph['label']
        report["number_of_nodes"] = len(chosenGraph.getVertrixes())
        report["number_of_edges"] = len(chosenGraph.getEdges())
        report["time_spent_in_miliseconds"] = t.get_timer_difference()
        report["origin_node"] = chosenGraph.getEntry().getData()
        report["distance_from_origin_to_each_node"] = executionResult['distances']
        report["predecessors_set"] = executionResult['predecessors']

        reportName = ntpath.split(chosenGraph['label'])
        with open('./reports/'+reportName+'report.txt', 'w') as file:
            file.write(json.dumps(report))
print("----------------------------------------------------------------------")
main()