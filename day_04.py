
txtFile = open('day_04.txt') #open('test_day_04.txt') 
lines = txtFile.readlines()


sumOverlap = 0
for line in lines:
    sectionPlan = line.strip()
    elvSections= sectionPlan.split(",")
    elvSections = [elvSections[0].split('-'), elvSections[1].split('-')]

    sect1IsIncluded_In2 = False
    sect2IsIncluded_In1 = False

    
    if int(elvSections[0][0]) >=int(elvSections[1][0]) and int(elvSections[0][1]) <= int(elvSections[1][1]):
        sect1IsIncluded_In2 = True
    elif int(elvSections[1][0]) >=int(elvSections[0][0]) and int(elvSections[1][1]) <= int(elvSections[0][1]):
        sect2IsIncluded_In1 = True

    if sect1IsIncluded_In2 == True or sect2IsIncluded_In1 == True:
        sumOverlap = sumOverlap +1

    for idxPair in range(2):
        sectView = ''
        for idxSection in range(100):
            if idxSection>=int(elvSections[idxPair][0]) and idxSection <= int(elvSections[idxPair][1]):
                sectView = sectView + f'{idxSection}'#chr(idxSection+0x30)
            else:
                sectView = sectView +'.'
        #print(f'{elvSections[idxPair]} {sectView} ==> {sect1IsIncluded_In2} {sect2IsIncluded_In1} --- {sumOverlap}')
    #print('')
#print(sumOverlap)

#################################################################################################################################################

sumOverlap = 0
for line in lines:
    sectionPlan = line.strip()
    elvSections= sectionPlan.split(",")
    elvSections = [elvSections[0].split('-'), elvSections[1].split('-')]

    segment1IsIncluded_In2 = False
    segment2IsIncluded_In1 = False

    
    if int(elvSections[0][0]) >=int(elvSections[1][0]) and int(elvSections[0][0]) <= int(elvSections[1][1]) \
        or int(elvSections[0][1]) >=int(elvSections[1][0]) and int(elvSections[0][1]) <= int(elvSections[1][1]):
        segment1IsIncluded_In2 = True
    elif int(elvSections[1][0]) >=int(elvSections[0][0]) and int(elvSections[1][0]) <= int(elvSections[0][1]) \
        or int(elvSections[1][1]) >=int(elvSections[0][0]) and int(elvSections[1][1]) <= int(elvSections[0][1]):
        segment2IsIncluded_In1 = True

    if segment1IsIncluded_In2 == True or segment2IsIncluded_In1 == True:
        sumOverlap = sumOverlap +1

    for idxPair in range(2):
        sectView = ''
        for idxSection in range(100):
            if idxSection>=int(elvSections[idxPair][0]) and idxSection <= int(elvSections[idxPair][1]):
                sectView = sectView + f'{idxSection}'#chr(idxSection+0x30)
            else:
                sectView = sectView +'.'
        print(f'{elvSections[idxPair]} {sectView} ==> {segment1IsIncluded_In2} {segment2IsIncluded_In1} --- {sumOverlap}')
    print('')
print(sumOverlap)