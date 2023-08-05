elvesList = []

with open('day_01.txt') as f:
    lines = f.readlines()

    jules = 0;
    maxJules = 0

    for line in lines:
        print(line.strip())
        if line.strip() == '':

            if jules > maxJules:
                maxJules = jules

            print(jules)
            elvesList.append(jules)
            jules=0
        else:
            jules = jules + int(line.strip())

    if jules > maxJules:
        maxJules = jules
    elvesList.append(jules)
elvesList.sort(reverse=True)

print(elvesList[0]+elvesList[1]+elvesList[2])


