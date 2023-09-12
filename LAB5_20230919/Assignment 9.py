print(' Drawing the square rectangular by "#" '.center(57, "-"))
print('[To quit this program by pressing "0"]')
print("-"*57)

while True:
    size = int(input("Please enter the size:"))
    if(size == 0):
        break
    
    for i in range(size):
        print("#"*i)
        for j in range(size):
            print("#", end="")
            print("#".rjust(i-1))
        if(size > 1):
            print("#"*i)