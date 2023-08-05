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
        self.resultNew = eval(self.operation) #e.g self.operation = 'old * 2 '
        return self.resultNew 

monkeyLst = []

for lineIdx, line in enumerate(lines):
    line = line.strip()
    if line.find("Monkey") != -1:
        monkeyLst.append(Monkey())

        monkeyLst[len(monkeyLst)-1].items = re.findall(r'\d+',lines[lineIdx+1]) 
        for itemIdx, item in enumerate(monkeyLst[len(monkeyLst)-1].items):
            monkeyLst[len(monkeyLst)-1].items[itemIdx] = int(item)
        
        monkeyLst[len(monkeyLst)-1].operation = lines[lineIdx+2][lines[lineIdx+2].find('=')+2: -1] 
        monkeyLst[len(monkeyLst)-1].tstFactor = int(re.findall(r'\d+',lines[lineIdx+3])[0])
        monkeyLst[len(monkeyLst)-1].tstOk = int(re.findall(r'\d+',lines[lineIdx+4])[0])
        monkeyLst[len(monkeyLst)-1].tstFail = int(re.findall(r'\d+',lines[lineIdx+5])[0])

# produkt aller Teiler für den chinesichen restsatz
allDivsMultipied = 1
for monkey in monkeyLst:
    allDivsMultipied *= monkey.tstFactor
# moduloAll = 

for round in range(10000):
    for monkey in monkeyLst:
        for line in range( len(monkey.items) ):
            monkey.inspectedItems += 1

            #chinesicher restsatz
            newItemValue = monkey.getNewResult( monkey.items.pop(0) ) % allDivsMultipied

            if newItemValue % monkey.tstFactor == 0:
                monkeyLst[ monkey.tstOk].items.append( newItemValue ) #int()int(newItemValue / monkey.tstFactor)
            else:
                monkeyLst[ monkey.tstFail].items.append( int(newItemValue) )
            

numberInspects = []
for monkey in monkeyLst:
    numberInspects.append(monkey.inspectedItems)
print(numberInspects )

numberInspects.sort(reverse=True)
print(numberInspects[0]*numberInspects[1] )


