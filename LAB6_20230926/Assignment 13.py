from random import randint

def start():
    number = randint(1, 99)
    floor = int(1)
    ceil = int(99)

    temp = int()

    hashStrap = "#".center(50, '#')
    tempStr = str()

    print(" Welcome to the game of guessing number ".center(50))

    for i in range(1, 6):
        print("round{}".format(i).center(50, '-'))
        
        temp = int(input("Enter an integer from {} to {} : ".format(floor, ceil)))
        
        if(temp == number):
            print(hashStrap)
            print("*** CONGRATULATION *** Your guess is correct".center(50))
            print(hashStrap)
            return
        
        tempStr = "Hint: Your guess is "
        
        if(temp < number):
            tempStr += "low"
            floor = temp
            
        else:
            tempStr += "high"
            ceil = temp
        
        print(tempStr)

    print(hashStrap)
    print("!!!SORRY!!! The secret number is {}".format(number).center(50))
    print(hashStrap)
    
start()
        