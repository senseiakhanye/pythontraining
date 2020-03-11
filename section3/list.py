myList = ["Katleho", "Archie", "Khanye"]
myList2 = ["Is", "writting", "python", "code"]
compactList = myList + myList2
print(compactList)

compactList[1] = compactList[1].upper()
print(compactList)

compactList.append("New Item")
print(compactList)

compactList.sort()
print(compactList)

compactList.pop(4)
print(compactList)