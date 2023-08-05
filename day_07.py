import re
import pprint

txtFile = open('day_07.txt')
lines = txtFile.readlines()

#Befehl $ cd /
#Befehl $ cd x
#Befehl $ cd ..
#Befehl $ ls

#info dir x
#info nnnn x.y
#info nnnn x

tdirData = {
                "a": 
                    { 
                    "e":
                        {
                            "i": 584
                        },
                        "f":29116,
                        "g":2557,
                        "h.lst":62596
                    },
                "b": 14848514,
                "c": 8504156,
                "d": 
                    {
                        "j":4060174, 
                        "d.log":8033020, 
                        "d.ext":5626152, 
                        "k":7214296
                    }
            }
#print(type(123))
dirSums = 0
possibleDirSize =[]
def getSizeDir(dirData:dict):
    global dirSums
    global possibleDirSize
    sumSize = 0
    #pprint.pprint(dirData)
    for dirElementName, dirElementValue  in dirData.items():
        if type(dirElementValue) is int:
            sumSize = sumSize + dirElementValue
        else:
            sumSize = sumSize + getSizeDir(dirData[dirElementName])

    if sumSize < 100000:
        dirSums = dirSums + sumSize
        #possibleDirSize.append(sumSize) #[ dirData.items()[0] ] = sumSize
    return sumSize

# Part 2 smalles directory >= space to free
def getSizeDir2(dirData:dict, tresHold:int):
    global possibleDirSize
    sumSize = 0
    #pprint.pprint(dirData)
    for dirElementName, dirElementValue  in dirData.items():
        if type(dirElementValue) is int:
            sumSize = sumSize + dirElementValue
        else:
            sumSize = sumSize + getSizeDir2(dirData[dirElementName], tresHold)

    if sumSize >= tresHold:
        possibleDirSize.append(sumSize) #[ dirData.items()[0] ] = sumSize
        #possibleDirSize[ dirData[0] ] = sumSize
        #dirSums = dirSums + sumSize
    return sumSize

#print( dirSums )
#print(getSizeDir(tdirData["a"] ), dirSums )


dirPointter = ''
dirLogger =[]
saveDir = False
dirData = {}
for line in lines:
    cmdLine = line.strip("\n")
    if cmdLine.find("$") != -1:
        saveDir = False
        if cmdLine.find("cd /")  != -1:
            dirPointter = dirData
            dirLogger= [ ]
        elif cmdLine.find("cd ..") != -1:
            dirPointter = dirLogger.pop() # = [ dirPointter ]
        elif cmdLine.find("cd ") != -1:
            dirLogger.append(dirPointter)
            #dirPointter = cmdLine[cmdLine.find("cd ")+3:]#new dir
            dirPointter = dirPointter[cmdLine[cmdLine.find("cd ")+3:]]
        elif cmdLine.find("ls") != -1:
            saveDir = True #save all lines untill next command
    else:
        if saveDir == True:
            if cmdLine.find("dir ") != -1:
                dirPointter[ cmdLine[ cmdLine.find("dir")+4: ] ] = {}
            else:
                fileData = cmdLine.split(' ')
                dirPointter[ fileData[1] ] = int(fileData[0])
                #dirData[ line[ line.find("dir")+4: ] ] 

#pprint.pprint(dirData)  
maxUsedSpace = getSizeDir( dirData )

#print(maxUsedSpace, dirSums ) #45717263 1084134
getSizeDir2(dirData , maxUsedSpace-40000000 )#maxUsedSpace-40000000
possibleDirSize.sort()
pprint.pprint( possibleDirSize[0] ) #6183184 min value
