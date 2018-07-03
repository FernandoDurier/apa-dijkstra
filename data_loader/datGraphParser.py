class datGraphParser:
    def __init__(self):
        pass

    def graphParserByArcs(self, path, beginString, endString, bidirectional):
       print("Path from graph parser by arcs: ", path)
       graphStruct = {
           "entry":[],
           "nodes":[],
           "edges":[]
       }
       with open(path) as fp:  
            line = fp.readline()
            cnt = 0
            edge = False
            end = False
            print(line)
            while line:
                
                if("LIST_OF_ARCS" in line.strip()):
                    edge = True
                    line = fp.readline()
                if(edge and ("END" in line.strip())):
                    end = True

                if( edge and not end):
                    cnt += 1
                    ed = line.strip().split()

                    if(cnt == 1): 
                        graphStruct['entry'] = 0

                    if(int(ed[1]) not in graphStruct['nodes']):
                        graphStruct['nodes'].append(int(ed[1]))

                    if(int(ed[0]) not in graphStruct['nodes']):
                        graphStruct['nodes'].append(int(ed[0]))
                    
                    edgeTuple = {"origin":int(ed[0]), "weigth":int(ed[2]), "end":int(ed[1])}
                    graphStruct['edges'].append(edgeTuple)
                    
                    if(bidirectional):
                        reverseEdge = {"origin":int(ed[1]), "weigth":int(ed[2]), "end":int(ed[0])}
                        graphStruct['edges'].append(reverseEdge)

                if(end):
                    return graphStruct

                line = fp.readline()
    
    def graphDatParser(self, path, bidirectional):
        return self.graphParserByArcs(path, "", "", bidirectional)

