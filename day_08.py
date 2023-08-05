txtFile = open('day_08.txt')
lines = txtFile.readlines()
dbgTxt = ''

def treeIsExposed(treeHight:int ,posX:int, posY:int):
    global lines
    leftOk = False
    rightOk = False
    aboveOk = False
    underOk = False


    treeLine = lines[posY].strip()

    #left hand side
    for treeXPos in range(posX-1, -1, -1): 
        if int(treeLine[treeXPos]) >= treeHight:
            leftOk = True
            break

    if leftOk == False:
        return False

    #right hand side
    for treeXPos in range(posX+1, len(treeLine), 1): 
        if int(treeLine[treeXPos]) >= treeHight:
            rightOk = True
            break
    if rightOk == False:
        return False

    #from top
    for treeYPos in range(posY-1, -1, -1): 
        if int(lines[treeYPos][posX]) >= treeHight:
            aboveOk = True
            break
    if aboveOk == False:
        return False
    
    #to buttom
    for treeYPos in range(posY+1, len(lines), 1): 
        if int(lines[treeYPos][posX]) >= treeHight:
            underOk = True
            break
    if underOk == False:
        return False

    return True

def treeScenicScore(posX:int, posY:int):
    global lines
    leftCnt = 0
    rightCnt = 0
    upCnt = 0
    downCnt = 0


    treeLine = lines[posY].strip()

    #left hand side
    for treeXPos in range(posX-1, -1, -1): 
        leftCnt = leftCnt + 1
        if int(treeLine[treeXPos]) >= int(lines[posY][posX]):
                break

    #right hand side
    for treeXPos in range(posX+1, len(treeLine), 1): 
        rightCnt = rightCnt + 1
        if int(treeLine[treeXPos]) >= int(lines[posY][posX]):
            break

    #from top
    for treeYPos in range(posY-1, -1, -1): 
        upCnt = upCnt +1
        if int(lines[treeYPos][posX]) >= int(lines[posY][posX]):
            break

    #to buttom
    for treeYPos in range(posY+1, len(lines), 1): 
        downCnt = downCnt +1
        if int(lines[treeYPos][posX]) >= int(lines[posY][posX]):
            break

    #print(lines[posY][posX], upCnt, leftCnt , downCnt, rightCnt )

    return leftCnt * rightCnt * upCnt * downCnt

exposedTreeCntr = 2*(len(lines)) + 2*(len(lines[0].strip())-2)
#print( exposedTreeCntr )
maxScenicScr = 0
for treePosY,line in enumerate(lines):
    if treePosY > 0 and treePosY < len(lines)-1:
        dbgTxt = ''
        treeLine = line.strip()
        for treePosX, treeHight in enumerate(treeLine):
            if treePosX > 0 and treePosX < len(treeLine)-1:

                #part 1
                # if treeIsExposed( int(treeHight) , treePosX, treePosY) == False:
                #     exposedTreeCntr = exposedTreeCntr +1
                #     dbgTxt = dbgTxt + 'x'
                # else:
                #     dbgTxt = dbgTxt + treeHight
                #part2
                tmpScenicScr = treeScenicScore(treePosX, treePosY)
                if maxScenicScr < tmpScenicScr:
                    maxScenicScr = tmpScenicScr
                    
        #print(dbgTxt)
#print(exposedTreeCntr)
print(maxScenicScr)

#print( treeScenicScore(2, 0))


# for tree in range(9, -1, -1):
#     print(tree)
