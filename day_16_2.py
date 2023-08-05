import re

txtFile = open('tday_16.txt') 
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
nodeVariationList = []
def goNode(aimNode, visitedNodeMemory,timeLeft, nodeMem):
    global nodeReducedDictList #nodeDictList
    global floydMarshalDict

    tmpNodeLst = visitedNodeMemory.copy()
    tmpNodeLst.append(aimNode)

    rateSum = timeLeft * nodeDictList[aimNode]['rate']
    rateSumLst =[]
 
    for NodeKey, NodeVlaue in nodeReducedDictList.items():
        newTimeLeft = (timeLeft-floydMarshalDict[aimNode][NodeKey]-1)
        if NodeKey not in tmpNodeLst and newTimeLeft > 0:
            retVal =  goNode(NodeKey, tmpNodeLst, newTimeLeft, nodeMem+';'+NodeKey )
            rateSumLst.extend( [rateSum + x for x in retVal])

    #last node in path is visited -> no further nodes avaliable
    if len(rateSumLst) == 0:
        rateSumLst.append( rateSum )
        #save all visited nodes to alist
        nodeVariationList.append(nodeMem.split(";"))
       
    #return rateSum
    return  rateSumLst.copy() 

#first run to get the best result and used nodes
possiblePaths = goNode('AA', [], 26, 'AA')

# get the list inde x of the path with the max vlaue
maxValue1st = max(possiblePaths) 
indexOfMax = 0
for pathIndx, pathVal in enumerate(possiblePaths):
    if maxValue1st == pathVal:
        indexOfMax = pathIndx

#remove the visited valves ( best path of the first run) 
for nodeKey in nodeVariationList[indexOfMax]:
    try:
        nodeReducedDictList.pop(nodeKey) # = {'rate': int(nodeFeatures[0][1]), 'neighbourLst':nodeNeighbours.split(",") }
    except:
        print(nodeKey, "node is not in list")
#print(nodeReducedDictList)

#perform another run but now without nodes from the first run
possiblePaths = goNode('AA', [], 26, 'AA')
maxValue2nd = max(possiblePaths)

print(maxValue1st+maxValue2nd) #2292 --> task 2





