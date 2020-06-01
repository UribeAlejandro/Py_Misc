def allLongestStrings(inputArray):
    longest=[]
    maxLen = 0
    for i in range(0,len(inputArray)):
        if maxLen < len(inputArray[i]):
            maxLen = len(inputArray[i])
    for i in range(0,len(inputArray)):
        if maxLen == len(inputArray[i]):
            longest.append(inputArray[i])
        return longest


inputArray = ["aba",
 "aa",
 "ad",
 "vcd",
 "aba"]
allLongestStrings(inputArray)