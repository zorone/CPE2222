print(' Drawing the square rectangular by "#" '.center(57, "-"))
print('[To quit this program by pressing "0"]')
print("-"*57)

while True:
    size = int(input("Please enter the size:"))
    if(size == 0):
        break
    
    print("#"*size)
    for i in range(size-2):
        print("#", end="")
        print("#".rjust(size-1))
    if(size > 1):
        print("#"*size)