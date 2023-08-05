import re

txtFile = open('tday_17.txt') 
lines = txtFile.readlines()

# list of the shapes witch are falling down
shapeList =  [
    [['####']],                 #-
    [['.#.'],['###'],['.#.']],  #+
    [['..#'],['..#'],['###']],  #L
    [['#'],['#'],['#'],['#']],  #|
    [['##'],['##']]             ##
]

shapeListDict =  {
    "-": {"wide": 4, "height": 1, "shape": ['####'] },              #-
    "+": {"wide": 3, "height": 3, "shape": ['.#.','###','.#.'] },   #+
    "L": {"wide": 3, "height": 3, "shape": ['..#','..#','###'] },   #L
    "|": {"wide": 1, "height": 4, "shape": ['#','#','#','#'] },     #|
    "#": {"wide": 2, "height": 2, "shape": ['##','##'] }            ##
}

#>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>

directionDic = {">": 1, "<":-1} #movement direction to the left or to the right
freeSlices = ['.......','.......','.......','.......']
caveHistoryList =['...#...','..###..','...#...']

def insertShapeAtPos(shape, posX, posY):
    tmpSlices = freeSlices.copy()

    for sliceIdx, slce in enumerate(tmpSlices):
        #if shape["height"] 
        print(sliceIdx)
        
    # for lineIdx in range(posY, 0, -1):
    #     tmpSlices[lineIdx] = tmpSlices[lineIdx][0:posX] + shape['shape'][(shape["height"]-lineIdx)] + tmpSlices[lineIdx][posX+shape["wide"]:]
        #print(lineIdx)
        #print(tmpSlices[lineIdx], shape["height"]-(lineIdx))
        #tmpSlices[lineIdx] = tmpSlices[lineIdx][0:posX] + shapeLine[(shape["height"]-lineIdx)] + tmpSlices[lineIdx][posX+shape["wide"]:]

    # for lineIdx, shapeLine in enumerate(shape["shape"]):
    #     tmpSlices[lineIdx] = tmpSlices[lineIdx][0:posX] + shapeLine[0] + tmpSlices[lineIdx][posX+shape["wide"]:]
    return tmpSlices

#insertShapeAtPos(shapeListDict["+"] , 1, 0)
threeLines = insertShapeAtPos(shapeListDict["+"] , 1, 3)
# for shapeLine in threeLines:
#     print(shapeLine)

def drawCave():

    for lineIdx in range(3):
        print("|", end="")
        for posIdx in range(7):
            print(".", end="")
        print("|")

    for sliceLine in caveHistoryList:
        print("|", end="")
        for sliceElmnt in sliceLine:
            print(sliceElmnt, end="")
        print("|")

    print("+-------+")

drawCave()
