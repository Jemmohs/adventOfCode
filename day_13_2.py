import re
txtFile = open('day_13.txt') 
lines = txtFile.readlines()

inputs = []
keyPattern =[ [[2]], [[6]]]
for line in lines:
    line = line.strip()
    if line != '':
        inputs.append(eval(line))


inputs.append(keyPattern[0])
inputs.append(keyPattern[1])
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

while(True):
    pocketsSorted = False
    for idx in range(0,(len(inputs)-1),1):

        if idx+1 < len(inputs):
            #print(f'{inputs[idx]}\n{inputs[idx+1]}\n')
            compRet = compareElement(inputs[idx], inputs[idx+1])

            if -1 == compRet:
                varTmp = inputs[idx+1].copy()
                inputs[idx+1] = inputs[idx]
                inputs[idx] = varTmp.copy()
                #cntr += (idx/2)+1
                pocketsSorted = True
    if pocketsSorted == False:
        break


#for Keyidx in range(2):
decoderKey = 0
firstKeyFound = False
for idx in range((len(inputs)-1)):

    if False == firstKeyFound and 0 == compareElement(inputs[idx], keyPattern[0]):
        decoderKey = idx+1
        firstKeyFound = True
        continue

    if True == firstKeyFound and 0 == compareElement(inputs[idx], keyPattern[1]):
        decoderKey *= idx+1
        break

# for idx in range(0,(len(inputs)-1),2):
#     print(f'{inputs[idx]}\n{inputs[idx+1]}')

print(decoderKey)

#print(int(cntr))

    
