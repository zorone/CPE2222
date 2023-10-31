def factorial(num):
    if(0 <= num <= 1):
        print(num)
    else:
        print(num*factorial(num-1))
        
factorial(10)