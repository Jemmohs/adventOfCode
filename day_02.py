"""
A = Rock
B = Paper
C = Scissors

X = Rock
Y = Paper
Z = Scissors

1 = Rock
2 = Paper
3 = Scissors

win = 6
los = 0
equal = 3

"""

elvesList = []

#stein/Papier   ->  6
#stein/Scherre  ->  0
#stein/Stein    ->  3


#Papier/Stein   ->  0
#Papier/papier  ->  3
#Papier/Scherre ->  6

#Scherre/Stein  -> 6
#Schrre/Papier  -> 0
#Scherre/Scherre -> 3




gameDict = {
    "AY": 6, #R/P 6
    "AZ": 0, #R/S 0
    "BX": 0, #P/R 0
    "BZ": 6, #P/S 6
    "CX": 6, #S/R 6
    "CY": 0, #S/P 0
}

scoreSum = 0
#with open('day_02.txt') as f:
    # lines = f.readlines()

    
    # for line in lines:
    #     myDraw = ord(line[2]) - ord('X') +1
    #     competatorDraw = ord(line[0]) - ord('A') +1

    #     if competatorDraw == myDraw:
    #         scoreSum = scoreSum + 3 + myDraw #+myDraw # gleichstand
    #     else:
    #         scoreSum = scoreSum + gameDict[f'{line[0]}{line[2]}']+ myDraw
    #     #R/R
    #         #R/P  3 -1 6 2
    #         #R/S  4 -2 0 2
    #         #P/R  3  1 0 4
    #     #P/P
    #         #P/S  5  1 6 6
    #         #S/R  3  2 6 5
    #         #S/P  5 -1 0 4
    #     #S/S

    #         #A-Y = 1 => Rock/Paper
    #         #A-Z = 2 => Rock/Scissors
    #         #paper = Scissors
    #         #Scissors/Paper
    #     #print(f'{line[0]} {line[2]} {competatorDraw} {myDraw} = {scoreSum}' )
    # #print( f'Score Sum = {scoreSum}' )

txtFile = open('day_02.txt') 
lines = txtFile.readlines()


#    #X lose -> 0
#    #Y tie -> 3
#    #Z win -> 6


strategy = 0
sumAllDraws = 0
for line in lines:

    isNotAtie = False
    strategy = 0

    if line[2] =='X': #lose
        strategy = 0
    elif line[2] =='Y': #tie
        strategy = 3
    else: #win
        strategy = 6

    for key,value in gameDict.items():
        if key[0] == line[0] and value == strategy:
            #print(f'{key[0]} {line[0]} {value} {strategy}')
            myDrawChar = key[1]
            myDraw = ord(myDrawChar) - ord('X') +1
            myDrawChar = chr( myDraw+0x40 )
            isNotAtie = True
            break
    
    if isNotAtie == False:
        myDrawChar = line[0]
        myDraw = ord(myDrawChar) - ord('A') +1
    sumDraw = (strategy+myDraw)
    sumAllDraws = sumAllDraws + sumDraw
    #print( f'{line[0]+line[2]}----{line[0]}{myDrawChar} => {strategy} + {myDraw} = {sumDraw} {sumAllDraws} .... {isNotAtie}')
    print(sumAllDraws)