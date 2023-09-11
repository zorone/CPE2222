A = str(input("Please enter the string A: "))
B = str(input("Please enter the string B: "))

print("-"*40)

setA = set(A)

setB = set(B)

bothAB = setA.intersection(setB)

onlyA = set()
onlyA = setA.difference(setB)

onlyB = set()
onlyB = setB.difference(setA)

notBoth = set()
notBoth = setA.symmetric_difference(setB)

all = set()
all = setA.union(setB)

print("A number of character in A is {}".format(len(A)))
print("A number of character in A is {}".format(len(B)))
print("A number of character in both A and B is {}".format(len(bothAB)))
print("Characters in A but not in B is {}".format(onlyA))
print("Characters in B but not in A is {}".format(onlyB))
print("Characters in A or B but not in both A and B is {}".format(notBoth))
print("All Characters in A and B is {}".format(all))