from ordered_linked_list.ordered_linked_list import *
from logger.timer import *
from graph_handler.edge import *
from graph_handler.vertrix import *
from graph_handler.graph import *
from dijkstra.closest_path import *
from dijkstra.closest_path_using_array import *
from data_loader.data_loader import *
import json
import ntpath
import gc

def main():

    graphs = []
    dl = Data_Loader()
    t = Timer()
    t2 = Timer()
    graphSet = dl.loadData('./problematic-data')

    for i in graphSet:
        g = Graph(Vertrix(i['entry']),i['name'],i['path'])
        for tup in i['edges']:
            #print("Edge: ", tup)
            g.addNewConnection(Vertrix(tup['origin']),tup['weigth'],Vertrix(tup['end']))
    
        print("-----------------------------------------------------------------------------------------------------")
        chosenGraph = g
        t.set_timer_start()
        print("-----------------------------------------------------------------------------------------------------")
        #print(" Adjacence List: ")
        grepresentation = chosenGraph.getRepresentation()
        #print(grepresentation)
        # for v in grepresentation['struct']:
        #     connections = grepresentation['struct'][v]['v'].getNexts()
        #     beautifulCon = []
        #     for c in connections:
        #         beauty = "["+str(c.getOrigin().getData())+","+str(c.getWeigth())+","+str(c.getEnd().getData())+"]"
        #         beautifulCon.append(beauty)
            #print("  [",grepresentation['struct'][v]['v'].getData(),"] = ", beautifulCon)
        
        executionResult = {}
        #executionResult = Dijkstra(chosenGraph.getRepresentation()['struct'],chosenGraph.getEntry().getData(),None)
        executionResult = DijkstraArray(chosenGraph.getRepresentation()['struct'],chosenGraph.getEntry().getData(),None)
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
        report["strategy"] = "using array"
        #report["strategy"] = "binheap priority queue"
        report["instance"] = grepresentation['label']
        report["number_of_nodes"] = len(chosenGraph.getVertrixes())
        report["number_of_edges"] = chosenGraph.getQuantityOfEdges()
        report["time_spent_in_miliseconds"] = t.get_timer_difference()
        start = chosenGraph.getEntry()
        report["origin_node"] = start.getData().getData()
        report["distance_from_origin_to_each_node"] = executionResult['distances']
        report["predecessors_set"] = executionResult['predecessors']
        #print("Report: ")
        #print(report)
        reportName = grepresentation['label'].replace("\\","-")
        with open('./reports/'+reportName+'report.txt', 'w') as file:
            for key, value in report.items():
                file.write('%s:%s\n' % (key, value))
            print("Completed Report for ", reportName)
        gc.collect()

main()