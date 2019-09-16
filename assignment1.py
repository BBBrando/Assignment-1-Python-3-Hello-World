
#Part 1 of assignment
def stringCount(aList):


    wordCount = dict()
    for word in aList:
        if word in wordCount:
            wordCount[word] += 1
        else:
            wordCount[word] = 1

    wordList = list(wordCount.keys())
    wordList = sorted(wordList, key=lambda s: s.lower())
    i = 0
    for word in wordCount:
        print(wordList[i], " ", wordCount[word])
        i=i+1
    return None

#Part 2 of assignment
def isFloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False
