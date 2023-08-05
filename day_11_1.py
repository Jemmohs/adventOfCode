import re
txtFile = open('day_11.txt')
lines = txtFile.readlines()

class Monkey:
    def __init__(self,items=[], operation='', tstFactor=0, tstOk=0, tstFail=0):
        self.items = items
        self.operation = operation
        self.tstFactor = tstFactor
        self.tstOk = tstOk
        self.tstFail = tstFail
        self.newResult = 0
        self.oldResult = 0
        self.inspectedItems = 0
    
    def getNewResult(self, old):
        #old = self.newResult
        self.resultNew = eval(self.operation) #e.g self.operation = 'old * 2 '
        return self.resultNew 

monkeyLst = []
#monkeyLst.append(Monkey([96, 60, 68, 91, 83, 57, 85],'old * 2',17,2,5))

for lineIdx, line in enumerate(lines):
    line = line.strip()
    if line.find("Monkey") != -1:
        monkeyLst.append(Monkey())
        # itemLst = re.findall(r'\d+',lines[lineIdx+1])
        # for number in itemLst:
        #     monkeyLst[len(monkeyLst)-1].items.append( int(number) )
        monkeyLst[len(monkeyLst)-1].items = re.findall(r'\d+',lines[lineIdx+1]) #.append( int(number) )
        for itemIdx, item in enumerate(monkeyLst[len(monkeyLst)-1].items):
            monkeyLst[len(monkeyLst)-1].items[itemIdx] = int(item)
        
        monkeyLst[len(monkeyLst)-1].operation = lines[lineIdx+2][lines[lineIdx+2].find('=')+2: -1] #' #old * 2'#re.findall(r'\d+',lines[lineIdx+2])[0]
        monkeyLst[len(monkeyLst)-1].tstFactor = int(re.findall(r'\d+',lines[lineIdx+3])[0])
        monkeyLst[len(monkeyLst)-1].tstOk = int(re.findall(r'\d+',lines[lineIdx+4])[0])
        monkeyLst[len(monkeyLst)-1].tstFail = int(re.findall(r'\d+',lines[lineIdx+5])[0])

for round in range(20):
    for monkey in monkeyLst:
        for line in range( len(monkey.items) ):
            monkey.inspectedItems += 1
            #devideTest = ( monkey.getNewResult( monkey.items[0]) // monkey.tstFactor)

            # devideble = False
            # if int(devideTest)*1000 == int(devideTest*1000):
            #     devideble = True 

            #devideResult = (monkey.getNewResult( monkey.items.pop(0) ) // 3)
            devideResult = (monkey.getNewResult( monkey.items.pop(0) ) /3 )
            newItemValue = int(devideResult)

            #devideTest = (  newItemValue / monkey.tstFactor)#monkey.getNewResult( monkey.items[0])
            devideble = False #int(newItemValue // monkey.tstFactor)*100 == int((100*newItemValue // monkey.tstFactor)):
            if newItemValue % monkey.tstFactor == 0:
                devideble = True 


            # #print( devideResult )
            # if int((devideResult - int(devideResult))*10) >= 5:
            #     newItemValue =  int(devideResult)+1
            # else:
            #     newItemValue =  int(devideResult)

            #print( devideResult, devideble )
            if devideble == True:
                monkeyLst[monkey.tstOk].items.append(newItemValue)
            else:
                monkeyLst[monkey.tstFail].items.append(newItemValue)
cntr = 0
    # print("-----------------------------------------------------")
# for monkey in monkeyLst:
#     print(cntr)
#     print(  "Inspects: ", monkey.inspectedItems     )
#     print(  "Items:    ", monkey.items    )
#     print(  "Operation ", monkey.operation)
#     print(  "tstFactor ", monkey.tstFactor)
#     print(  "tstOk:    ", monkey.tstOk    )
#     print(  "tstFail:  ", monkey.tstFail  )
#     print(  "newResult:", monkey.newResult)
#     print(  "oldResult:", monkey.oldResult)
#     print()
#     cntr += 1


#print(newItemValue, devideble)
        
#monkeyLst[1].items.append( )
#print(monkeyLst[0].getNewResult(10) )

#print(posLst[posIdx], posLst[posIdx]-posLst[posIdx-1])
cntr = 0
numberInspects = []
for monkey in monkeyLst:
    numberInspects.append(monkey.inspectedItems)
#print(numberInspects)
numberInspects.sort(reverse=True)
print(numberInspects[0]*numberInspects[1] )
    # print(cntr)
    # print(  "Inspects: ", monkey.inspectedItems     )
    # # print(  "Items:    ", monkey.items    )
    # # print(  "Operation ", monkey.operation)
    # # print(  "tstFactor ", monkey.tstFactor)
    # # print(  "tstOk:    ", monkey.tstOk    )
    # # print(  "tstFail:  ", monkey.tstFail  )
    # # print(  "newResult:", monkey.newResult)
    # # print(  "oldResult:", monkey.oldResult)
    # print()
    # cntr += 1