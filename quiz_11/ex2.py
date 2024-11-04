nLines = int(input(""))

strList = list()

mostCharacters = 0
idxMostCharacters = 0

for idx in range(nLines):
    newLine = input("")

    if len(newLine) > mostCharacters:
        mostCharacters = len(newLine)
        idxMostCharacters = idx

    strList.append(newLine)

anwserList = list()

for idx in range(len(strList)):
    anwserList.append("")


for idx in range(nLines):
    if idx == idxMostCharacters: 
        anwserList[idx] = strList[idx]
        continue
    nCharacters = len(strList[idx])

    nSpacesToBeAdded = mostCharacters - nCharacters

    strList[idx] = strList[idx].split(" ")
    
    nWords = len(strList[idx])

    rest = nSpacesToBeAdded % (nWords - 1)


    spacePerChar = int(nSpacesToBeAdded / (nWords - 1))

    for i in range(len(strList[idx]) - 1):
        anwserList[idx] += strList[idx][i] + " " * (spacePerChar + 1)
        if rest > 0:
            anwserList[idx] += " "
            rest += -1
    
    anwserList[idx] += strList[idx][len(strList[idx]) - 1]
    
for idx in range(len(anwserList)):
    print(anwserList[idx])





