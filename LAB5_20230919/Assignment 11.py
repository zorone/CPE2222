print("Making a list of Factorial series of n")
n = int(input("Enter 'n' of Factorial number:"))
arr = [1]

for i in range(2, n+1):
    arr += [arr[i-1] * i]

print("A list of Factorial series of {} is {}".format(n, arr))