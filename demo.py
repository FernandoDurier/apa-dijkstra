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
    graphSet = dl.loadData('./demo-data')

    for i in graphSet:
        g = Graph(Vertrix(i['entry']),i['name'],i['path'])
        for tup in i['edges']:
            #print("Edge: ", tup)
            g.addNewConnection(Vertrix(tup['origin']),tup['weigth'],Vertrix(tup['end']))
    
        print("-----------------------------------------------------------------------------------------------------")
        chosenGraph = g
        grepresentation = chosenGraph.getRepresentation()
        #print("-----------------------------------------------------------------------------------------------------")
        # print(" Adjacence List: ")
        
        # #print(grepresentation)
        # for v in grepresentation['struct']:
        #     connections = grepresentation['struct'][v]['v'].getNexts()
        #     beautifulCon = []
        #     for c in connections:
        #         beauty = "["+str(c.getOrigin().getData())+","+str(c.getWeigth())+","+str(c.getEnd().getData())+"]"
        #         beautifulCon.append(beauty)
        #     print("  [",grepresentation['struct'][v]['v'].getData(),"] = ", beautifulCon)
        # print("------------------------------------------------------------------------------------------------------")
        
        t.set_timer_start()
        executionResult1 = {}
        #executionResult = Dijkstra(chosenGraph.getRepresentation()['struct'],chosenGraph.getEntry().getData(),None)
        executionResult1 = DijkstraArray(chosenGraph.getRepresentation()['struct'],chosenGraph.getEntry().getData(),None)
        t.set_timer_end()
        report1 = {}
        
        start = chosenGraph.getEntry()
        report1["strategy"] = "using array"
        report1["instance"] = grepresentation['label']
        report1["number_of_nodes"] = len(chosenGraph.getVertrixes())
        report1["number_of_edges"] = chosenGraph.getQuantityOfEdges()
        report1["time_spent_in_miliseconds"] = t.get_timer_difference()
        report1["origin_node"] = start.getData().getData()
        report1["distance_from_origin_to_each_node"] = executionResult1['distances']
        report1["predecessors_set"] = executionResult1['predecessors']
        
        t.set_timer_start()
        executionResult2 = {}
        executionResult2 = Dijkstra(chosenGraph.getRepresentation()['struct'],chosenGraph.getEntry().getData(),None)
        #executionResult = DijkstraArray(chosenGraph.getRepresentation()['struct'],chosenGraph.getEntry().getData(),None)
        t.set_timer_end()

        report2 = {}
        report2["strategy"] = "binheap priority queue"
        report2["instance"] = grepresentation['label']
        report2["number_of_nodes"] = len(chosenGraph.getVertrixes())
        report2["number_of_edges"] = chosenGraph.getQuantityOfEdges()
        report2["time_spent_in_miliseconds"] = t.get_timer_difference()
        report2["origin_node"] = start.getData().getData()
        report2["distance_from_origin_to_each_node"] = executionResult2['distances']
        report2["predecessors_set"] = executionResult2['predecessors']

        print("----------------------------------------------------------------")
        print("Report1: ", report1['instance'])
        #print(report1)
        print("----------------------------------------------------------------")
        print("Report2: ", report2['instance'])
        #print(report2)
        print("----------------------------------------------------------------")
        
        reportName1 = report1['instance'].replace("\\","-")
        with open('./reports/demo/demo-'+reportName1+' '+report1['strategy']+' report.txt', 'w') as file:
            for key, value in report1.items():
                file.write('%s:%s\n' % (key, value))
            print("Completed Report for ", reportName1)

        reportName2 = report2['instance'].replace("\\","-")
        with open('./reports/demo/demo-'+reportName2+' '+report2['strategy']+' report.txt', 'w') as file:
            for key, value in report2.items():
                file.write('%s:%s\n' % (key, value))
            print("Completed Report for ", reportName2)
        
        gc.collect()

main()