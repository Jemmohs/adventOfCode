txtFile = open('day_09.txt') #'day_09.txt')
lines = txtFile.readlines()

commandLst = []

for line in lines:
    commandLst.append( {"dir":line[0], "stps": int(line[1:])} )

knotsNumber = 2
knotPosList = []
tailPoses = [{"x":10,"y":10}]

for idx in range(knotsNumber):
    knotPosList.append({"x":10,"y":10})

def printSnapShot():
    playFieldPic = ''
    knotName = ''
    global knotPosList
    global knotsNumber

    for yPos in range (25,-1,-1): #6
        for xPos in range (25): #6
            knotName = ''
            for knotIdx in range(knotsNumber-1,-1,-1):
                if knotIdx == 0 and knotPosList[0]["x"] == xPos and knotPosList[0]["y"] == yPos:
                    knotName = 'H'
                elif knotPosList[knotIdx]["x"] == xPos and knotPosList[knotIdx]["y"] == yPos:
                    knotName = f'{knotIdx}'

            if knotName == '':
                knotName = '.'

            playFieldPic = playFieldPic + knotName 
        playFieldPic = playFieldPic +'\n'
    print(playFieldPic,"\n")

#printSnapShot()

def moveHead(command:dict, knot:int):
    global knotPosList
    if command["dir"] == 'R' or command["dir"] == 'L':

        if command["dir"] == 'R':
            knotPosList[knot]["x"] = knotPosList[knot]["x"] +1
        else:
            knotPosList[knot]["x"] = knotPosList[knot]["x"] -1

    elif command["dir"] == 'U' or command["dir"] == 'D' :

        if command["dir"] == 'U':
            knotPosList[knot]["y"] = knotPosList[knot]["y"] +1
        else:
            knotPosList[knot]["y"] = knotPosList[knot]["y"] -1
    else:
        print("no direction found")
        return

def checkPos(pos:dict):
    for tailPos in tailPoses:
        if tailPos == pos:
            return False
    return True

def moveTail(command:dict, knot:int):

    global knotPosList
    dirStepX = 1
    dirStepY = 1
    tmpX = knotPosList[knot]["x"]
    tmpY = knotPosList[knot]["y"]

    if abs(knotPosList[knot]["x"] - knotPosList[knot-1]["x"]) == 2:
        dirStepX = 1
        if knotPosList[knot-1]["x"] > knotPosList[knot]["x"]:
            dirStepX = -1
        tmpX = knotPosList[knot-1]["x"] + dirStepX

        if knotPosList[knot]["y"] != knotPosList[knot-1]["y"]:
            tmpY = knotPosList[knot-1]["y"]

    if abs(knotPosList[knot]["y"] - knotPosList[knot-1]["y"]) == 2:
        dirStepY = 1
        if knotPosList[knot-1]["y"] > knotPosList[knot]["y"]:
            dirStepY = -1
        tmpY = knotPosList[knot-1]["y"] + dirStepY
        if abs(knotPosList[knot]["x"] - knotPosList[knot-1]["x"]) == 2:
            tmpX = knotPosList[knot-1]["x"]+ dirStepX
        else:
            tmpX = knotPosList[knot-1]["x"]
    
    if knot == (knotsNumber-1) and (knotPosList[knot]["x"] != tmpX or knotPosList[knot]["y"] != tmpY):
        if checkPos({"x":tmpX,"y":tmpY}) == True:
            tailPoses.append({"x":tmpX,"y":tmpY})
        
    knotPosList[knot]["x"] = tmpX
    knotPosList[knot]["y"] = tmpY

def moveRope( knotNumber:int):
    global knotsNumber
    global knotPosList
    global tailPoses
        
    knotsNumber = knotNumber
    knotPosList = []
    tailPoses = [{"x":10,"y":10}]

    for idx in range(knotsNumber):
        knotPosList.append({"x":10,"y":10})

    for cmdIdx in range(len(commandLst)):
            
            #print(f'===== {commandLst[cmdIdx]["dir"]} {commandLst[cmdIdx]["stps"]} =====')
            for PosIdx in range( commandLst[cmdIdx]["stps"]):
                moveHead(commandLst[cmdIdx],0)
                for knotIdx in range(1,knotsNumber,1):
                    moveTail(commandLst[cmdIdx], knotIdx)
            #printSnapShot() #print grafical view of the points
    print(f'Knots:{knotNumber}, diff. tail positions: {len(tailPoses)}')

#knotsNumber = 2  5513
moveRope(2)
#knotsNumber = 10 2427
moveRope(10)
