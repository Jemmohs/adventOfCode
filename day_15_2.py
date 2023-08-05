import re
from collections import defaultdict

txtFile = open('day_15.txt') 
lines = txtFile.readlines()

inputSensorMap = defaultdict(lambda: ".")
radarMap = defaultdict(lambda: ".")

minPosX = 9999999999
maxPosX = 0
minPosY = 9999999999
maxPosY = 0

txtOutput = ''

# read input data and get min/max of the x/y coordinates
for line in lines:
    coordinates =  re.findall(r'-?\d+',line)
    sensorPosX, sensorPosY, beaconPosX, beaconPosY = int(coordinates[0]), int(coordinates[1]), int(coordinates[2]), int(coordinates[3]) 
    inputSensorMap[f"{sensorPosX},{sensorPosY}"] = [int(coordinates[2]), int(coordinates[3]) ]
    radarMap[f"{sensorPosX},{sensorPosY}"] = 'S'
    radarMap[f"{beaconPosX},{beaconPosY}"] = 'B'

    maxPosX = max([maxPosX, sensorPosX, beaconPosX] )
    minPosX = min([minPosX, sensorPosX, beaconPosX] )
    maxPosY = max([maxPosY, sensorPosY, beaconPosY] )
    minPosY = min([minPosY, sensorPosY, beaconPosY] )

#print (inputSensorMap)
#print(minPosX, maxPosX, minPosY, maxPosY)
#print( inputSensorMap.values())


def printMap(minX,maxX, minY, maxY):
    global txtOutput
    global radarMap

    #make x axis labels
    txtOutput = "    "
    for posX in range(minX,maxX+1,1):
         txtOutput += str(posX % 10)
    txtOutput +="\n"

    for posY in range(minY,maxY+1,1):
        #make y-axis labels
        txtOutput +=f'{posY:03d} '
        #make x/y points
        for posX in range(minX,maxX+1,1):
            txtOutput += radarMap[f"{posX},{posY}"]#radarMap[posY][posX]
        txtOutput +="\n"
    print(txtOutput)


def drwRadius(sensX, sensY, mhtRadius):
    newRadius = mhtRadius
    for lvlY in range(0,newRadius,1):
        #upper part
        #right side
        if radarMap[f"{mhtRadius -lvlY+sensX},{sensY-lvlY}"] =='.':
            radarMap[f"{mhtRadius -lvlY+sensX},{(sensY-lvlY)}"] = '#'
        #left side
        if radarMap[f"{sensX-(mhtRadius -lvlY)},{sensY-lvlY}"] =='.':
            radarMap[f"{sensX-(mhtRadius -lvlY)},{(sensY-lvlY)}"] = '#'
        
        #lower part
        #right side
        if radarMap[f"{(mhtRadius -lvlY)+sensX},{sensY+lvlY}"] =='.':
            radarMap[f"{mhtRadius -lvlY+sensX},{(sensY+lvlY)}"] = '#'
        #left side
        if radarMap[f"{sensX-(mhtRadius -lvlY)},{sensY+lvlY}"] =='.':
            radarMap[f"{sensX-(mhtRadius -lvlY)},{(sensY+lvlY)}"] = '#'

    #peaks of lower and upper part
    if radarMap[f"{sensX},{sensY-newRadius}"] =='.':
        radarMap[f"{sensX},{sensY-newRadius}"]= '#'

    if radarMap[f"{sensX},{sensY+newRadius}"] =='.':
        radarMap[f"{sensX},{sensY+newRadius}"] = '#'

# #Test map view 
# for sensorKey, beaconPos in inputSensorMap.items():

#     sensPos = sensorKey.split(",")
#     sensPosX, sensPosY = int(sensPos[0]) , int(sensPos[1])
#     mhtRadius = abs(sensPosX - beaconPos[0]) + abs(sensPosY - beaconPos[1])

#     maxPosX = max([maxPosX, sensPosX+mhtRadius] )
#     minPosX = min([minPosX, sensPosX-mhtRadius] )
#     maxPosY = max([maxPosY, sensPosY+mhtRadius] )
#     minPosY = min([minPosY, sensPosY-mhtRadius] )

#     for radius in range(1,mhtRadius+1,1):
#         drwRadius(sensPosX , sensPosY, radius)
#     #printMap(minPosX, maxPosX, minPosY, maxPosY)

# cntr = 0
# for posX in range(minPosX,maxPosX+1,1):
#     if radarMap[f"{posX},{10}"] == "#":
#         cntr+=1

# printMap(minPosX, maxPosX, minPosY, maxPosY)
# print(cntr)

rangesList = []

def mergeRanges(rngMin, rngMax):

    global rangesList
    tmpRngMax = 0
    tmpRngMin = 0
    fial = False
    if len(rangesList) > 0:
        for rng in rangesList:
            if rngMin <= rng[0] :
                tmpRngMin = rngMin
                if rngMax >= rng[1]:
                    tmpRngMax = rngMax
                    rng[0] = tmpRngMin
                    rng[1] = tmpRngMax
                    fial = False

                elif rngMax <= rng[1] and rngMax >= rng[0]:
                    tmpRngMax = rng[1]
                    rng[0] = tmpRngMin
                    rng[1] = tmpRngMax
                    fial = False
                else:
                    fial = True
            elif rngMin >= rng[0] and rngMin <= rng[1]:
                tmpRngMin = rng[0]
                tmpRngMax = rngMax
                if rngMax < rng[1]:
                    tmpRngMax = rng[1]

                rng[0] = tmpRngMin
                rng[1] = tmpRngMax
                fial = False
            else:
                fial = True 

    if len(rangesList) == 0 or fial == True:
        rangesList.append([rngMin, rngMax])

myRanges = []
rngCntr = 0
def mergeRangesByList():

    global rangesList
    global myRanges
    newRangeMerged = False
    tmpRngMin, tmpRngMax = rangesList.pop(0)

    while True:
        newRangeMerged = False

        for rngIdx in range(len(rangesList)):
            if tmpRngMin <= rangesList[rngIdx][0]:
                if tmpRngMax >= rangesList[rngIdx][1]:
                    rangesList.pop(rngIdx)
                    newRangeMerged = True
                    break

                elif tmpRngMax <= rangesList[rngIdx][1] and tmpRngMax >= rangesList[rngIdx][0]:
                    tmpRngMax = rangesList[rngIdx][1]
                    rangesList.pop(rngIdx)
                    newRangeMerged = True
                    break

            elif tmpRngMin >= rangesList[rngIdx][0] and tmpRngMin <= rangesList[rngIdx][1]:
                tmpRngMin = rangesList[rngIdx][0]
                if tmpRngMax < rangesList[rngIdx][1]:
                    tmpRngMax = rangesList[rngIdx][1]

                rangesList.pop(rngIdx)
                newRangeMerged = True
                break

        if newRangeMerged == False: #no connectet range found
            myRanges.append([tmpRngMin, tmpRngMax])
            if len(rangesList) != 0:
                tmpRngMin, tmpRngMax = rangesList.pop(0)
            else:
                break   


def getRadiusAtPos(sensX, sensY, mhtRadius, targetPos):

    targetPos = abs(sensY - targetPos) #get absolute distance to the beacon on the y Axis
    lineRange = [(mhtRadius -targetPos+sensX), (sensX-(mhtRadius -targetPos))] #get x position range max to min
    lineRange.sort() #sort elements (min, max)

    #mergeRanges(lineRange[0], lineRange[1])

    return lineRange


lineRangeMinX = 9999999999999999999
lineRangeMaxX = 0
targetLine = 3400528#22 <<-- line with the gap
maxSearchPosY = 4000000

for lineIdx in range(maxSearchPosY): #ca 10 min :(
    targetLine = lineIdx
    myRanges = []
    rangesList = []

    for sensorKey, beaconPos in inputSensorMap.items():
        sensPos = sensorKey.split(",")
        sensPosX, sensPosY = int(sensPos[0]) , int(sensPos[1])
        mhtRadius = abs(sensPosX - beaconPos[0]) + abs(sensPosY - beaconPos[1])

        if abs(sensPosY - targetLine) <= mhtRadius:
            lineRangeX= getRadiusAtPos(sensPosX, sensPosY, mhtRadius, targetLine)
            #print(lineRangeX)
            lineRangeMinX = min( [lineRangeMinX, lineRangeX[0] ] )
            lineRangeMaxX = max( [lineRangeMaxX, lineRangeX[1] ] )
            rangesList.append([lineRangeX[0] , lineRangeX[1]])
            #print(sensorKey, lineRangeX[0] , lineRangeX[1])

    mergeRangesByList()
    if len(myRanges) != 1:
        print(myRanges, lineIdx )
        if  myRanges[0][1] < myRanges[1][1]:
            print("gap at :", myRanges[0][1]+1, lineIdx, ((myRanges[0][1]+1)*maxSearchPosY)+lineIdx )
        else:
            print("gap at :", myRanges[1][1]+1, lineIdx, ((myRanges[1][1]+1)*maxSearchPosY)+lineIdx )
             
        break 

# gtX = 3141837
# gtEerg = 12567351400528 #x * 4000000 + y
# gtY = 12567351400528 -(4000000*gtX) #3400528
# print(gtY)
# if len(myRanges) > 1:
#     if  myRanges[0][1] < myRanges[1][1]:
#         print("gap at :", myRanges[0][1]+1)#(myRanges[1][0] - myRanges[0][1])+myRanges[0][1] )
#     else:
#         print("gap at :", myRanges[1][1]+1)#(myRanges[0][0] - myRanges[1][1])+myRanges[1][1] )
        
# hh = ''.join(radarMap['11'])
# # print(lineRangeMinX, lineRangeMaxX, hh  )

# # number of al possible positions
# numberPositions = (lineRangeMaxX - lineRangeMinX+1) 
# beaconInTargetLn = []

# #subtract beacons from the possible position number
# for sensorKey, beaconPos in inputSensorMap.items():

#     if beaconPos[1] not in beaconInTargetLn:
#         beaconInTargetLn.append( beaconPos[1] )
#         if  beaconPos[1] == targetLine and (beaconPos[0] <= lineRangeMaxX and beaconPos[0] >= lineRangeMinX):
#             numberPositions -=1;

# print(numberPositions, lineRangeMinX, lineRangeMaxX ) #6078701 -1161321 4917380

# #printMap(minPosX, maxPosX, minPosY, maxPosY)


