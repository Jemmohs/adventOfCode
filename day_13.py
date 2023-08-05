import re
txtFile = open('day_13.txt') 
lines = txtFile.readlines()

inputs = []
for line in lines:
    line = line.strip()
    if line != '':
        inputs.append(eval(line))

"""
links kleiner als rechts
links == rechts -> nechster vergleich
links hat (beim verglichen) weniger elemet als Rechts
wenn eine zahl mit einer kiste verglichen wird  -> wird die zahl in eine Liste gewandelt
"""
def compareElement(elmL, elmR):

    if isinstance(elmL, int) and isinstance(elmR, int):
        if elmL == elmR:
            return 0
        elif elmL < elmR:
            return 1
        else:
            return -1

    elif isinstance(elmL, int) and not isinstance(elmR, int):
        elmL = [elmL]

    elif not isinstance(elmL, int) and isinstance(elmR, int):
        elmR = [elmR]

    minElem = min(len(elmL), len(elmR) )

    for idx in range(minElem ):
            compRet= compareElement(elmL[idx], elmR[idx])
            if compRet != 0:
                return compRet  
            
    return compareElement(len(elmL), len(elmR))


cntr = 0
for idx in range(0,(len(inputs)-1),2):

    #print(f'{inputs[idx]}\n{inputs[idx+1]}\n')
    compRet = compareElement(inputs[idx], inputs[idx+1])

    if 1 == compRet:
        cntr += (idx/2)+1

print(int(cntr))

    
