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


def getRadiusAtPos(sensX, sensY, mhtRadius, targetPos):

    targetPos = abs(sensY - targetPos) #get absolute distance to the beacon on the y Axis
    lineRange = [(mhtRadius -targetPos+sensX), (sensX-(mhtRadius -targetPos))] #get x position range max to min
    lineRange.sort() #sort elements (min, max)

    return lineRange


lineRangeMinX = 9999999999999999999
lineRangeMaxX = 0
targetLine = 2000000 #10

for sensorKey, beaconPos in inputSensorMap.items():
    sensPos = sensorKey.split(",")
    sensPosX, sensPosY = int(sensPos[0]) , int(sensPos[1])
    mhtRadius = abs(sensPosX - beaconPos[0]) + abs(sensPosY - beaconPos[1])

    if abs(sensPosY - targetLine) <= mhtRadius:
        lineRangeX= getRadiusAtPos(sensPosX, sensPosY, mhtRadius, targetLine)
        #print(lineRangeX)
        lineRangeMinX = min( [lineRangeMinX, lineRangeX[0] ] )
        lineRangeMaxX = max( [lineRangeMaxX, lineRangeX[1] ] )
        #print(sensorKey, lineRangeX[0] , lineRangeX[1])


# number of al possible positions
numberPositions = (lineRangeMaxX - lineRangeMinX+1) 
beaconInTargetLn = []

#subtract beacons from the possible position number
for sensorKey, beaconPos in inputSensorMap.items():

    if beaconPos[1] not in beaconInTargetLn:
        beaconInTargetLn.append( beaconPos[1] )
        if  beaconPos[1] == targetLine and (beaconPos[0] <= lineRangeMaxX and beaconPos[0] >= lineRangeMinX):
            numberPositions -=1;

print(numberPositions, lineRangeMinX, lineRangeMaxX ) #6078701 -1161321 4917380

#printMap(minPosX, maxPosX, minPosY, maxPosY)


