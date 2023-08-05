txtFile = open('day_10.txt') #'day_09.txt')
lines = txtFile.readlines()

#noop = 1 cy
#addx =2 cy

opLst = []
opData = {"noop":1,"addx":2}
regX = 1
cycleCntr = 0
cycleIntr = 40
sigStrength = 0

sprite ='###'
videoLine =""


#EJCFPGLH
for line in lines:
    opertaions = line.strip().split(" ")
    if len(opertaions) == 2:
        opLst.append( {"op":opertaions[0], "param": int(opertaions[1])} )
    else:
        opLst.append( {"op":opertaions[0], "param": 0} )
    
for opertaion in opLst:
    for cycle in range(opData[opertaion["op"]]):
        cycleCntr = cycleCntr +1
        if cycleCntr%40 >= regX and cycleCntr%40 < (regX+3):
            videoLine = videoLine +'#'
        else:
           videoLine = videoLine +'.' 
        #print(cycleCntr,regX)
        if cycleCntr == cycleIntr:
            print(videoLine)
            videoLine = ""

            cycleIntr = cycleIntr +40
        if opData[opertaion["op"]] == cycle+1 and opertaion["op"] == "addx":
            regX = regX+opertaion["param"]
        
        