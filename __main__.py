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

    for tup in set1:
        g1.addNewConnection(Vertrix(int(tup[0])),int(tup[2]),Vertrix(int(tup[1])))

    print("------------------------")
    print("Adjacence List for G1: ")
    for v in g1.getVertrixes():
        connections = v.getNexts()
        beautifulCon = []
        for c in connections:
            beauty = "["+str(c.getOrigin().getData())+","+str(c.getWeigth())+","+str(c.getEnd().getData())+"]->"
            beautifulCon.append(beauty)
        print("[",v.getData(),"] = ", beautifulCon)
    


    g2 = Graph(Vertrix(int(set2[0][0])))

    for tup in set2:
        g2.addNewConnection(Vertrix(int(tup[0])),int(tup[2]),Vertrix(int(tup[1])))

    print("------------------------")
    print("Adjacence List for G2: ")
    for v in g2.getVertrixes():
        connections = v.getNexts()
        beautifulCon = []
        for c in connections:
            beauty = "["+str(c.getOrigin().getData())+","+str(c.getWeigth())+","+str(c.getEnd().getData())+"]->"
            beautifulCon.append(beauty)
        print("[",v.getData(),"] = ", beautifulCon)
    


    g3 = Graph(Vertrix(int(set3[0][0])))

    for tup in set3:
        g3.addNewConnection(Vertrix(int(tup[0])),int(tup[2]),Vertrix(int(tup[1])))

    print("------------------------")
    print("Adjacence List for G3: ")
    for v in g3.getVertrixes():
        connections = v.getNexts()
        beautifulCon = []
        for c in connections:
            beauty = "["+str(c.getOrigin().getData())+","+str(c.getWeigth())+","+str(c.getEnd().getData())+"]->"
            beautifulCon.append(beauty)
        print("[",v.getData(),"] = ", beautifulCon)



    g4 = Graph(Vertrix(int(set4[0][0])))

    for tup in set4:
        g4.addNewConnection(Vertrix(int(tup[0])),int(tup[2]),Vertrix(int(tup[1])))

    print("------------------------")
    print("Adjacence List for G4: ")
    for v in g4.getVertrixes():
        connections = v.getNexts()
        beautifulCon = []
        for c in connections:
            beauty = "["+str(c.getOrigin().getData())+","+str(c.getWeigth())+","+str(c.getEnd().getData())+"]->"
            beautifulCon.append(beauty)
        print("[",v.getData(),"] = ", beautifulCon)
    

main()