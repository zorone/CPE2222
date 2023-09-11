A = str(input("Please enter the string A: "))
B = str(input("Please enter the string B: "))

print("-"*40)

Alist = A.split()
Blist = B.split()

bothAB = set()
bothAB = Alist.intersection(Blist)

onlyA = set()
onlyA = Alist.difference(Blist)

onlyB = set()
onlyB = Blist.difference(Alist)

notBoth = set()
notBoth = Alist.symmetric_difference(Blist)

all = set()
all = Alist.union(Blist)

print("A number of character in A is {}".format(len(A)))
print("A number of character in A is {}".format(len(B)))
print("A number of character in both A and B is {}".format(len(bothAB)))
print("Characters in A but not in B is {}".format(onlyA))
print("Characters in B but not in A is {}".format(onlyB))
print("Characters in A or B but not in both A and B is {}".format(notBoth))
print("All Characters in A and B is {}".format(all))