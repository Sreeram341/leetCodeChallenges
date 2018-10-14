"""
Input:
4
bcdef
abcdefg
bcde
bcdef
"""

words = int(input())
wordsLis = []
for i in range(words):
    wordsLis.append(input())

def wordOrder(listOfWords):
    fistWord =listOfWords[0]
    lenOfFirstWord = len(fistWord)
    distinctDict = {}
    distinctDict[fistWord]=1
    for i in range(1, len(listOfWords)):
        if len(listOfWords[i]) > lenOfFirstWord:
            if listOfWords[i] in distinctDict:
                distinctDict[listOfWords[i]] += 1
                #if fistWord in combos(listOfWords[i], lenOfFirstWord):
                 #   distinctDict[fistWord] += 1
            else:
                distinctDict[listOfWords[i]] = 1
                #if fistWord in combos(listOfWords[i], lenOfFirstWord):
                 #   distinctDict[fistWord] += 1
        else:
            if len(listOfWords[i]) == lenOfFirstWord and listOfWords[i] == lenOfFirstWord:
                distinctDict[listOfWords[i]] += 1
            else:
                if listOfWords[i] in distinctDict:
                    distinctDict[listOfWords[i]] += 1
                else:
                    distinctDict[listOfWords[i]] = 1
    print(len(distinctDict))
    print(' '.join('{}'.format(val) for val in sorted(distinctDict.values(),reverse=True)))


def combos(inpStr, fixLen):
    inpLis = list(inpStr)
    inpLen = len(inpLis)
    fixLen = fixLen-1
    retLis=[]
    for i in range(inpLen):
        for j in range(i+1, inpLen):
            if j+fixLen <= inpLen:
                retLis.append("".join(inpLis[i]+inpStr[j:j+fixLen]))
    return retLis


if __name__ == "__main__":
    wordOrder(wordsLis)

