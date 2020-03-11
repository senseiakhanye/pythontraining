
#for loops in range
iter = [2, 5, 6, 7, 10]
for value in iter:
    print("Number : " + str(value))
print()

#String loops
str = "Katleho Khanye"
for letter in str:
    print(letter)

#turple pairs
tuplePair = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 19)]
for item in tuplePair:
    print(item)

for a, b in tuplePair:
    print(a)
    print(b)
    print()

#dictionary 
d = {'K1': 1, 'k2': 2, 'k3': 3}
print()
print("Print items as is")
for item in d.items():
    print(d)
print()
print("Keys ...")
for keys in d.keys():
    print(keys)
print()
print("Values ...")
for values in d.values():
    print(values)

#Create a list from a string (new method learned later in same section)
myList = []
print(myList)