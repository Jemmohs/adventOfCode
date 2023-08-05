import copy
txtFile = open('tday_09.txt') #'day_09.txt')
lines = txtFile.readlines()

commandLst = []

for line in lines:
    commandLst.append( {"dir":line[0], "stps": int(line[1:])} )

posHead = {"x":50,"y":50}
posTail = {"x":50,"y":50}
oldPosHead = {"x":50,"y":50}

posHead = {"x":5,"y":5}
posTail = {"x":5,"y":5}
oldPosHead = {"x":5,"y":5}

knotPosList = []

for idx in range(10):
    knotPosList.append({"x":0,"y":0})
#knotPosList = [{"x":5,"y":5}] * 10

tailPosList = [copy.deepcopy(posTail) ]

#matrix 5x6
# def printSnapShot():
#     playFieldPic = ''
#     for yPos in range (10,-1,-1): #4
#         for xPos in range (10): #6
#             if posHead["x"] == xPos and posHead["y"] == yPos:
#                 playFieldPic = playFieldPic +'H'
#             elif posTail["x"] == xPos and posTail["y"] == yPos:
#                 playFieldPic = playFieldPic +'T'
#             else:
#                 playFieldPic = playFieldPic +'.'
#         playFieldPic = playFieldPic +'\n'
#     #print(playFieldPic,"\n")

def printSnapShot():
    playFieldPic = ''
    knotName = ''
    for yPos in range (6,-1,-1): #25
        for xPos in range (6): #25
            for knotIdx in range(9,-1,-1):
                if knotIdx == 0 and knotPosList[0]["x"] == xPos and knotPosList[0]["y"] == yPos:
                    knotName = 'H'
                elif knotPosList[knotIdx]["x"] == xPos and knotPosList[knotIdx]["y"] == yPos:
                    knotName = f'{knotIdx}'
                else:
                    knotName = '.'
            playFieldPic = playFieldPic + knotName 
        playFieldPic = playFieldPic +'\n'
    print(playFieldPic,"\n")

printSnapShot()
def addTailPosition(tailPos:dict):
    for postion in tailPosList:
        if postion == tailPos:
            #print(postion, tailPos)
            return
    tailPosList.append(tailPos)


def moveHead(command:dict):
    global posHead
    global posTail
    #print(f'===== {command["dir"]} {command["stps"]} =====')
    
    for idx in range( command["stps"] ):
        oldPosHead["x"] = posHead["x"]
        oldPosHead["y"] = posHead["y"]

        if command["dir"] == 'R' or command["dir"] == 'L':
            if command["dir"] == 'R':
                posHead["x"] = posHead["x"] +1
            else:
                posHead["x"] = posHead["x"] -1

            if abs(posHead["x"] - posTail["x"]) == 2:
                posTail["x"] = oldPosHead["x"]
                if posHead["y"] != posTail["y"]:
                    posTail["y"] = oldPosHead["y"]
                addTailPosition(copy.deepcopy(posTail))
        elif command["dir"] == 'U' or command["dir"] == 'D' :
            if command["dir"] == 'U':
                posHead["y"] = posHead["y"] +1
            else:
                posHead["y"] = posHead["y"] -1

            if (abs(posHead["y"] - posTail["y"]) == 2 and posHead["x"] != posTail["x"]) \
                or posHead["x"] == posTail["x"] and abs(posHead["y"] - posTail["y"]) == 2:
                posTail = copy.deepcopy(oldPosHead)
                addTailPosition(copy.deepcopy(posTail))
        else:
            print("no direction found")
            return
        printSnapShot()


def moveHead2(command:dict, knot:int):
    global posHead
    global posTail
    print(f'===== {command["dir"]} {command["stps"]} =====')
    
    if knot == 9:
        return

    for idx in range( command["stps"] ):
        oldPosHead["x"] = knotPosList[knot]["x"]
        oldPosHead["y"] = knotPosList[knot]["y"]

        if command["dir"] == 'R' or command["dir"] == 'L':

            if command["dir"] == 'R':
                knotPosList[knot]["x"] = knotPosList[knot]["x"] +1
            else:
                knotPosList[knot]["x"] = knotPosList[knot]["x"] -1
            ## loop 1-9
            if abs(knotPosList[knot]["x"] - knotPosList[knot+1]["x"]) == 2:
                knotPosList[knot+1]["x"] = oldPosHead["x"]
                if knotPosList[knot]["y"] != knotPosList[knot+1]["y"]:
                    knotPosList[knot+1]["y"] = oldPosHead["y"]
                ##call moveHead2
                moveHead2(command, knot+1 )
                #addTailPosition(copy.deepcopy(knotPosList[knot+1]))
        elif command["dir"] == 'U' or command["dir"] == 'D' :

            if command["dir"] == 'U':
                knotPosList[knot]["y"] = knotPosList[knot]["y"] +1
            else:
                knotPosList[knot]["y"] = knotPosList[knot]["y"] -1

            ## loop 1-9
            if (abs(knotPosList[knot]["y"] - knotPosList[knot+1]["y"]) == 2 and knotPosList[knot]["x"] != knotPosList[knot+1]["x"]) \
                or knotPosList[knot]["x"] == knotPosList[knot+1]["x"] and abs(knotPosList[knot]["y"] - knotPosList[knot+1]["y"]) == 2:
                ##call moveHead2
                moveHead2(command, knot+1 )
                #posTail = copy.deepcopy(oldPosHead)
                #addTailPosition(copy.deepcopy(posTail))
        else:
            print("no direction found")
            return
        printSnapShot()

for cmdIdx in range(len(commandLst)):#
    moveHead2(commandLst[cmdIdx],0)

print( len(knotPosList))

#print(len(tailPosList))
