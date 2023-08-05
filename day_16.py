import re

txtFile = open('day_16.txt') 
lines = txtFile.readlines()


#Valve AA has flow rate=0; tunnels lead to valves DD, II, BB

nodeDictList = {}
nodeReducedDictList = {}
nodeBitDictList = {}
cntr = 0
for line in lines:
    nodeFeatures =  re.findall(r'Valve ([A-Z][A-Z]) has flow rate=(\d+);.*?([A-Z].*[A-Z])',line)
    nodeNeighbours = nodeFeatures[0][2].replace(" ", "")
    
    nodeDictList[nodeFeatures[0][0]] = {'rate': int(nodeFeatures[0][1]), 'neighbourLst':nodeNeighbours.split(",") }
    if int(nodeFeatures[0][1]) > 0:
        nodeReducedDictList[nodeFeatures[0][0]] = {'rate': int(nodeFeatures[0][1]), 'neighbourLst':nodeNeighbours.split(",") }
        nodeBitDictList[nodeFeatures[0][0]] = (1<<cntr)
        cntr+=1

#print(nodeBitDictList)

#create and init the Marshal Matrix
FloydWarshallMatrix = [ [0]*len(nodeDictList) for i in range(len(nodeDictList))]
floydMarshalDict = {}

for node in nodeDictList:
    floydMarshalDict[node] = {}
    for neighNode in nodeDictList:
        if neighNode == node:
            floydMarshalDict[node][neighNode] = 0
        elif neighNode in nodeDictList[node]['neighbourLst']:
            floydMarshalDict[node][neighNode] = 1
        else:
            floydMarshalDict[node][neighNode] = 9999


for warshalStep in nodeDictList: # horizontale 
    for horizonatlNode in nodeDictList: #verticale
        for verticalNode in nodeDictList: #einezelen nodes in der horizontale
            
            floydMarshalDict[verticalNode][horizonatlNode] = min([floydMarshalDict[verticalNode][horizonatlNode],
                                                                  (floydMarshalDict[verticalNode][warshalStep]+
                                                                   floydMarshalDict[warshalStep][horizonatlNode])  ])

def goNode(aimNode, visitedNodeMemory,timeLeft):
    global nodeReducedDictList #nodeDictList
    global floydMarshalDict

    tmpNodeLst = visitedNodeMemory.copy()
    tmpNodeLst.append(aimNode)

    rateSum = timeLeft * nodeDictList[aimNode]['rate']
    rateSumLst =[]
 
    for NodeKey, NodeVlaue in nodeReducedDictList.items():
        newTimeLeft = (timeLeft-floydMarshalDict[aimNode][NodeKey]-1)
        if NodeKey not in tmpNodeLst and newTimeLeft > 0:
            rateSumLst.append( rateSum + goNode(NodeKey, tmpNodeLst, newTimeLeft ))
    
    if len(rateSumLst) > 0:
         rateSum = max( rateSumLst )
       
    return rateSum
    
print(goNode('AA', [], 30)) #1828