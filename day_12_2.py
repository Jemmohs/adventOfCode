import re
import sys

sys.setrecursionlimit(5000)
txtFile = open('day_12.txt') 
lines = txtFile.readlines()


mapRecord = [] 
mapPointDB = [] 
for lineIdx, line in enumerate(lines):
    mapRecord.append( line.strip() )

# print(mapRecord[20][120])
# print(mapRecord[20][0])

#print( len(mapRecord) )

class Point:
    def __init__(self,height, posX, posY):
        self.dir = {} #{"<":None, ">":None, "^":None, "v":None }

        self.height = height
        self.posX = posX
        self.posY = posY
        self.visited = False
        self.kost = 0xFFFFF
        self.previousNode = None



def getHeight(charHeight):
    if charHeight == 'E':
        charHeight = ord('z')-0x61
    elif charHeight == 'S':
        charHeight = ord('a')-0x61
    else:
        charHeight = ord(charHeight)-0x61
    return charHeight

aKoordinates = {}

def getApositions():
    for posY in range(len(mapRecord)):
        for posX in range(len(mapRecord[posY])):
            if mapRecord[posY][posX] == 'a' or mapRecord[posY][posX] == 'S':
                aKoordinates[f'{posX},{posY}']  = [posX,posY]

getApositions()
#print(aKoordinates)


# test
MyMapPoints = { "0,0": Point('a', 0, 0) }
MyMapPoints["0,0"].kost = 0
myNodeQueue = [MyMapPoints["0,0"]]

# MyMapPoints = { "0,20": Point('a', 0, 20) }
# MyMapPoints["0,20"].kost = 0
# myNodeQueue = [MyMapPoints["0,20"]]

def getNeighbours(pnt):
    currentHight = getHeight( mapRecord[pnt.posY][pnt.posX]) 

    neighBourHight = 0
    posX = 0
    posYOffset = 0
    dirChar = ""
    for dirIdx in range(4):
        posX = 0
        posY = 0
        if dirIdx == 0:
            posX = -1
            dirChar = "<"
        elif dirIdx == 1:
            posX = 1
            dirChar = ">"
        elif dirIdx == 2:
            posY = -1
            dirChar = "^"
        else:
            posY = 1
            dirChar = "v"

        posX += pnt.posX
        posY += pnt.posY

        if ((posY >= 0) and (posY < len(mapRecord) )) and ((posX >= 0) and (posX < len(mapRecord[posY]) )):

            newHeight = getHeight( mapRecord[posY][posX])
        
            if abs( currentHight - newHeight ) <= 1 or currentHight > newHeight:
                if(f"{posX},{posY}" not in MyMapPoints):
                    pnt.dir[f"{dirChar}"] = Point(mapRecord[posY][posX], posX, posY )
                    MyMapPoints[f"{posX},{posY}"] = pnt.dir[f"{dirChar}"]
    return pnt.dir

playField = [] #['.......',".......",".......",".......","......."]
for line in range(len(mapRecord)):
    txt = ""
    for chars in range(len(mapRecord[0])):
        txt += "."
    playField.append(txt)

kostList = []
for koordinateKey, koordinateValue in aKoordinates.items():

    MyMapPoints = { koordinateKey: Point('a', koordinateValue[0], koordinateValue[1]) }
    MyMapPoints[koordinateKey].kost = 0
    myNodeQueue = [MyMapPoints[koordinateKey]]

    while( len(myNodeQueue) != 0):

        if myNodeQueue[0].visited == False:
            neighbourNodes = getNeighbours(myNodeQueue[0])

            for NodeNeighboursKey, NodeNeighboursValue in neighbourNodes.items():

                if NodeNeighboursValue.kost > (myNodeQueue[0].kost + 1):
                    NodeNeighboursValue.kost = myNodeQueue[0].kost + 1
                    NodeNeighboursValue.previousNode = myNodeQueue[0]
                    #playField[myNodeQueue[0].posY] = playField[myNodeQueue[0].posY][:myNodeQueue[0].posX] + NodeNeighboursValue.height+ playField[myNodeQueue[0].posY][myNodeQueue[0].posX + 1:]
                    #playField[myNodeQueue[0].posY] = playField[myNodeQueue[0].posY][:myNodeQueue[0].posX] + NodeNeighboursKey+ playField[myNodeQueue[0].posY][myNodeQueue[0].posX + 1:]
                    myNodeQueue[0].visited = True

                    if NodeNeighboursValue.height == 'E':
                        kostList.append( NodeNeighboursValue.kost )
                        #print(kostList)
                        #print(NodeNeighboursValue.kost)
                    if NodeNeighboursValue.visited == False:
                        myNodeQueue.append( NodeNeighboursValue )
                else:
                    playField[myNodeQueue[0].posY] = playField[myNodeQueue[0].posY][:myNodeQueue[0].posX] + "x"+ playField[myNodeQueue[0].posY][myNodeQueue[0].posX + 1:]

            myNodeQueue.pop(0)
kostList.sort()
print(kostList[0])
# for NodeNeighboursKey, NodeNeighboursValue in MyMapPoints.items():
#     print( NodeNeighboursKey )

#print(MyMapPoints["5,2"].kost)

# for line in playField:
#     print(line)

#print(MyMapPoints["120,20"].kost)

















