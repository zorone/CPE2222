print('  Drawing the right triangle by "*"  '.center(50, "-"))
print('[To quit this program by pressing "0"]')
print("-"*50)

n = int(input("Enter the height of right triangle:"))

while n != 0:
    if n > 1:
        print("*".rjust(n))
    for i in range(1, n-1):
        print("*".rjust(n-i), "*")
    print("*"*n)
    
    n = int(input("Enter the height of right triangle:"))