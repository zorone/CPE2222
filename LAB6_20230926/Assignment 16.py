import math

table = {'Circle': dict(), 'Square': dict(), 'Triangle': dict()}

def dictGen(size :int):
    for l in range (1, size+1):
        circleArea = math.pi*(l**2)
        squareArea = l**2
        triangleArea = (3**(1/2))*(l**2)*(1/4)
        
        for keys in ('Circle', 'Square', 'Triangle'):
            table[keys].update({l: circleArea})


def main():
    size = 100
    dictGen(size)
    pageBreak = '-'*50
    
    while True:
        print("Enter the geometry shape for an area calculation")
        print("[Circle, Square, Triangle]")
        shape = str(input("[Enter something else to exit this program]:")).title()
        
        if shape not in table.keys():
            return
        
        print("Enter the dictionary key")
        index = round(float(input("{} - {}:".format(1, size))))
        
        if index not in range(1, size+1):
            print("!!! The key is out of scope !!!")
            return
        
        print(pageBreak)
        print("The area of {} is {}".format(shape.upper(), table[shape][index]))
        print(pageBreak)

main()