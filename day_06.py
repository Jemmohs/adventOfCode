testData = ["mjqjpqmgbljsphdztnvjfqwrcgsmlb",
"bvwbjplbgvbhsrlpgdmjqwftvncz",
"nppdvjthqldpwncqszvftbrmjlhg",
"nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg",
"zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"]

def getMsgBeginnIdx(dataSet:str, equalChars:int):
    equalFound = False
    msgBeginn = ''
    for idx in range(len(dataSet)):
        if(idx > (equalChars-1)):
            equalFound = False
            msgBeginn = dataSet[idx-equalChars:idx]
            dbgTxt = '' 
            for cmpCharIdx in range(equalChars):
                for chrIdx in range(equalChars):
                    if cmpCharIdx != chrIdx and dataSet[idx-cmpCharIdx-1] == dataSet[idx-chrIdx-1]:
                        dbgTxt =dbgTxt + f'{dataSet[idx-cmpCharIdx-1]} {dataSet[idx-chrIdx-1]}\n'
                        equalFound = True
                        break
            if equalFound != True:
                return msgBeginn,idx
                #print("YAP---->",idx)
                #break

# for tData in testData:
#     print("4 MSG_Beginn:", getMsgBeginnIdx(tData,4))
#     print("14 MSG_Beginn:", getMsgBeginnIdx(tData,14))

txtFile = open('day_06.txt') #open('test_day_04.txt') 
msgBuffer = txtFile.read()
print("4 MSG_Beginn:", getMsgBeginnIdx(msgBuffer,4))
print("14 MSG_Beginn:", getMsgBeginnIdx(msgBuffer,14))

