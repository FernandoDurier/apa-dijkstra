class steinlibParser:
    def __init__(self):
        pass

    def graphParserByEdges(self, path, beginString, endString, bidirectional):
       #print("Path from graphParserByEdges: ", path)
       graphStruct = {
           "path":path,
           "entry":[],
           "nodes":[],
           "edges":[]
       }
       with open(path) as fp:  
            line = fp.readline()
            cnt = 0
            edge = False
            end = False
            while line:
                
                if("Edges " in line.strip()):
                    edge = True
                if(edge and ("End" in line.strip())):
                    end = True

                if( not end and "E " in line.strip()):
                    cnt += 1
                    ed = line.strip().split()

                    if(cnt == 1): 
                        graphStruct['entry'] = ed[1]

                    if(int(ed[1]) not in graphStruct['nodes']):
                        graphStruct['nodes'].append(int(ed[1]))

                    if(int(ed[2]) not in graphStruct['nodes']):
                        graphStruct['nodes'].append(int(ed[2]))
                    
                    edgeTuple = {"origin":int(ed[1]), "weigth":int(ed[3]), "end":int(ed[2])}
                    graphStruct['edges'].append(edgeTuple)
                    
                    if(bidirectional):
                        reverseEdge = {"origin":int(ed[2]), "weigth":int(ed[3]), "end":int(ed[1])}
                        graphStruct['edges'].append(reverseEdge)

                if(end):
                    return graphStruct

                line = fp.readline()
    
    def graphParser(self, path, bidirectional):
        return self.graphParserByEdges(path, "", "", bidirectional)

