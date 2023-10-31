def factorial(num):
    if(0 <= num <= 1):
        print(num)
        return num
    else:
        num *= factorial(num-1)
        print(num)
        return num
        
factorial(10)