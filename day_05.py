import re

txtFile = open('day_05.txt') #open('test_day_04.txt') 
lines = txtFile.readlines()


def getStacks():
    stacks = []
    stackCntr = 0
    for line in lines:
        stackCntr = 0
        if line[1] != '1':
            for idx in range(0,len(line.strip("\n")),4):

                packName = line[ (stackCntr*4+1):(stackCntr*4+2) ]
                
                try:
                    stacks[stackCntr].append(packName)
                except:
                    stacks.append([ packName ])
                stackCntr = stackCntr+1
        else:
            break 

    #clear empty spaces
    for stack in stacks:
        for idx, stackPos in enumerate(stack):
            if stackPos != ' ':
                del stack[0: idx]
                break

    
    #print(stacks)

    # lineTxt = ''
    # for rowIdx in range(len(stacks[0])):
    #     lineTxt = ''
    #     for stack in stacks:
    #         lineTxt = lineTxt + f'[{stack[rowIdx]}]'
    #     print(lineTxt)

    return  stacks

def getMoveOperations():
    moveOperations = []
    for line in lines:
        if line.find("move") != -1:
            moveOperations.append(re.findall(r'\d+',line))
    #print(moveOperations)
    return moveOperations

moveOperations = getMoveOperations()
boxStacks = getStacks()

print (boxStacks,"\n")

##### part 1 #####
# for operation in moveOperations:
#     for idx in range(int(operation[0])):
#         boxStacks[ int(operation[2])-1  ].insert(0, boxStacks[ int(operation[1])-1 ][idx])
#     del boxStacks[ int(operation[1])-1 ][0:int(operation[0])]

##### part 2 #####
for operation in moveOperations:
    boxStacks[ int(operation[2])-1  ][0:0] = boxStacks[ int(operation[1])-1 ][0: int(operation[0])]
    del boxStacks[ int(operation[1])-1 ][0:int(operation[0])]


stackCode = ''
for boxStack in boxStacks:
    stackCode  = stackCode + boxStack[0]

print (boxStacks,"\n")
print(stackCode)




