
txtFile = open('day_03.txt') #open('test_day_03.txt') 
lines = txtFile.readlines()
rucksSackItems = []
sumItemPriority = 0

for line in lines:
    rueckSack = line.strip()
    posSecondCompart= int(len(rueckSack)/2)
    #print(rueckSack, posSecondCompart)
    sameItem = ''
    comItemfound = False

    for itemNameCm1 in range(posSecondCompart):
        if sameItem == '':
            for itemNameCm2 in range(posSecondCompart):
                if rueckSack[itemNameCm1] == rueckSack[itemNameCm2+posSecondCompart]:
                    sameItem = sameItem + rueckSack[itemNameCm1]
                    rucksSackItems.append( rueckSack[itemNameCm1] )
                    break
        else:
            break

    itemCode =ord(sameItem) - ord('a')
    if itemCode < 0:
        itemCode = ord(sameItem) - ord('A') + 27
    else:
        itemCode = itemCode + 1

    sumItemPriority = sumItemPriority + itemCode
    #print(f'{rueckSack} === {rueckSack[:posSecondCompart]}  {rueckSack[posSecondCompart:]}  {sameItem} -- {itemCode} -- {sumItemPriority}')

    #################################################################################################################################################

lineCntr = 0
sumItemBadge = 0
while( lineCntr < len(lines)):
    print(f'{lines[lineCntr].strip()}\n{lines[lineCntr+1].strip()}\n{lines[lineCntr+2].strip()}')
    sameItem = ''
    for ruckSac1kItem in lines[lineCntr]:
        if sameItem == '':
            for ruckSack2Item in lines[lineCntr+1]:
                if ruckSac1kItem == ruckSack2Item:
                    for ruckSack3Item in lines[lineCntr+2]:
                        if ruckSack2Item == ruckSack3Item:
                            sameItem = ruckSack3Item
                            break
        else:
            break
    
    itemCode =ord(sameItem) - ord('a')
    if itemCode < 0:
        itemCode = ord(sameItem) - ord('A') + 27
    else:
        itemCode = itemCode + 1

    sumItemBadge = sumItemBadge + itemCode

    print(f'===> {sameItem} {itemCode} {sumItemBadge} \n')

    lineCntr = lineCntr +3

print( sumItemBadge )
# for line in lines:
#     rueckSack = line.strip()
#     posSecondCompart= int(len(rueckSack)/2)
#     #print(rueckSack, posSecondCompart)
#     sameItem = ''
#     comItemfound = False

#     for itemNameCm1 in range(posSecondCompart):
#         if sameItem == '':
#             for itemNameCm2 in range(posSecondCompart):
#                 if rueckSack[itemNameCm1] == rueckSack[itemNameCm2+posSecondCompart]:
#                     sameItem = sameItem + rueckSack[itemNameCm1]
#                     rucksSackItems.append( rueckSack[itemNameCm1] )
#                     break
#         else:
#             break

#     itemCode =ord(sameItem) - ord('a')
#     if itemCode < 0:
#         itemCode = ord(sameItem) - ord('A') + 27
#     else:
#         itemCode = itemCode + 1

#     sumItemPriority = sumItemPriority + itemCode
#     print(f'{rueckSack} === {rueckSack[:posSecondCompart]}  {rueckSack[posSecondCompart:]}  {sameItem} -- {itemCode} -- {sumItemPriority}')