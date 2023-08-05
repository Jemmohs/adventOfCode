import re
txtFile = open('day_14.txt') 
lines = txtFile.readlines()

minPosX = 9999999999
maxPosX = 0
minPosY = 9999999999
maxPosY = 0

mapList = {}
stoneList =[]

for lineIdx, line in enumerate(lines):
    line = line.strip() #get rid of \r\n
    stoneList.append( [] )
    for koordinate in line.split("->"):
        koordinate = koordinate.strip() #get rid of Spaces
        kordinateList = koordinate.split(",") #get the kordinates X Y
        mapList[koordinate] = [int(kordinateList[0]), int(kordinateList[1])]
        stoneList[lineIdx].append( [int(kordinateList[0]), int(kordinateList[1])] )

        #get map Ranges
        if minPosX > mapList[koordinate][0]:
            minPosX = mapList[koordinate][0]
        if maxPosX < mapList[koordinate][0]:
            maxPosX = mapList[koordinate][0]

        if minPosY > mapList[koordinate][1]:
            minPosY = mapList[koordinate][1]
        if maxPosY < mapList[koordinate][1]:
            maxPosY = mapList[koordinate][1]

maxPosY+=2 # for the extra floor
#add aditional floor layer
stoneList.append( [[minPosX, maxPosY], [maxPosX, maxPosY] ] )

        

#print(mapList)
#print(minPosX, maxPosX, minPosY, maxPosY)
myRoomMap =[]

txtOutput = ""
for numberSlice in range(3):
    #txtOutput.append([])
    txtOutput += "    "
    for rowIdx in range(maxPosX -minPosX+1):
        txtOutput += str(minPosX+rowIdx)[numberSlice]
    txtOutput += "\n"
        #[numberSlice].append(str(minPosX+rowIdx)[numberSlice])

#print(txtOutput)
for posY in range(maxPosY+1):
    myRoomMap.append([])
    for posX in range(maxPosX-minPosX+1):
        myRoomMap[posY].append(".")



def insertStones():
    global stoneList
    global myRoomMap

    numberStones  = 0
    driction = 1
    startPosX = -1
    startPosY = -1

    for stoneLines in stoneList:
        for stoneLineIdx in range(1, len(stoneLines),1):
            if stoneLines[stoneLineIdx-1][0] != stoneLines[stoneLineIdx][0]:
                driction = -1
                #print(stoneLines[stoneLineIdx-1][0])
                if (stoneLines[stoneLineIdx-1][0] - stoneLines[stoneLineIdx][0]) < 0:
                    driction = 1
                
                startPos = (stoneLines[stoneLineIdx-1][0]-minPosX)
                stopPos = (stoneLines[stoneLineIdx][0]-minPosX)

                for i in range(startPos, stopPos , driction): # -1 to reach 0
                    myRoomMap[stoneLines[stoneLineIdx-1][1]][i] = '#'

                #korner cases sometimes not reached by the loop
                myRoomMap[stoneLines[stoneLineIdx-1][1]][startPos] = '#'
                myRoomMap[stoneLines[stoneLineIdx-1][1]][stopPos] = '#'
            if stoneLines[stoneLineIdx-1][1] != stoneLines[stoneLineIdx][1]:
                driction = -1
                #print(stoneLines[stoneLineIdx-1][0])
                if (stoneLines[stoneLineIdx-1][1] - stoneLines[stoneLineIdx][1]) < 0:
                    driction = 1
                
                startPos = (stoneLines[stoneLineIdx-1][1])
                stopPos = (stoneLines[stoneLineIdx][1])
                #print(f"{stoneLines[stoneLineIdx-1][0]}-{minPosX} = {startPos}")
                #print(f"{stoneLines[stoneLineIdx][0]}-{minPosX} = {stopPos}")
                for i in range(startPos, stopPos , driction):
                    myRoomMap[i][stoneLines[stoneLineIdx-1][0]-minPosX] = '#'
                
                #korner cases sometimes not reached by the loop
                myRoomMap[startPos][stoneLines[stoneLineIdx-1][0]-minPosX] = '#'
                myRoomMap[stopPos][stoneLines[stoneLineIdx-1][0]-minPosX] = '#'


                
def printMap():
    global txtOutput
    global myRoomMap
    for posY in range(len(myRoomMap)):
        txtOutput +=f'{posY:03d} '
        for posX in range(len(myRoomMap[0])):
            txtOutput += myRoomMap[posY][posX]
        txtOutput +="\n"
    print(txtOutput)

#def insertFloor():

enterPos = (500 - minPosX)

def getCenterPos():
    for rowIdx, row in enumerate(myRoomMap):
        if row[enterPos] != '.':
            return (rowIdx-1)
        
def addRow(rightSide):
    global myRoomMap
    global enterPos
    if False == rightSide:
        for lineIdx, line in enumerate(myRoomMap):
            myRoomMap[lineIdx].insert(0, '.')
        myRoomMap[len(myRoomMap)-1][0] = '#'
        enterPos +=1
    else:
        for lineIdx, line in enumerate(myRoomMap):
            myRoomMap[lineIdx].append('.')
        myRoomMap[len(myRoomMap)-1][len(myRoomMap[0])-1] = '#';



insertStones()
#printMap()

moveDir = 0 # 0 = center, 1 = left, 2 = right
restPosFound = False
lastCenterPos = getCenterPos()
sandPosX = enterPos
sandPosY = 0 #lastCenterPos
leftIsRest = False
rightIsRest = False
sandGrindInRest = False

cntr = 0
#for sandGrind in range(26):
while sandGrindInRest == False:
    # if sandGrindInRest == True:
    #     break

    sandPosX = enterPos
    sandPosY = 0
    while sandGrindInRest == False:

        if  sandPosY >=len( myRoomMap) or sandPosY < 0:
            sandGrindInRest = True
            
        if sandPosX >= len(myRoomMap[0]):
            addRow(True)
            continue
        elif sandPosX <0 :
            addRow(False)
            sandPosX = 0
            continue

            #sandGrindInRest = True

        
        if myRoomMap[sandPosY][sandPosX] == '.':
            sandPosY +=1
            continue
        else:
            if (sandPosX-1) >= 0 and myRoomMap[sandPosY][sandPosX-1] == '.':
                sandPosX -=1
            elif (sandPosX+1) < len(myRoomMap[0]) and myRoomMap[sandPosY][sandPosX+1] == '.':
                sandPosX +=1
            else:
                if (sandPosX-1) < 0:
                    addRow(rightSide= False)
                    sandPosX = 1
                elif (sandPosX+1) >= len(myRoomMap[0]):
                    addRow(rightSide= True)
                  #sandGrindInRest = True
                  #break
                else:            
                    myRoomMap[sandPosY-1][sandPosX] = 'o'
                    cntr +=1
                    if sandPosY-1 == 0:
                        sandGrindInRest = True
                    break

printMap()
print(cntr)