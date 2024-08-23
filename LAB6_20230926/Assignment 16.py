import math

table = {'Circle': dict(), 'Square': dict(), 'Triangle': dict()}

keys = ('Circle', 'Square', 'Triangle')

def dictGen(size :int):
    for l in range (1, size+1):
        areas = (math.pi*(l**2), )
        areas += (l**2, )
        areas += ((3**(1/2))*(l**2)*(1/4), )
        
        for i in range(3):
            table[keys[i]].update({l: areas[i]})


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
        index = math.floor(float(input("{} - {}:".format(1, size))))
        
        if index not in range(1, size+1):
            print("!!! The key is out of scope !!!")
            return
        
        print(pageBreak)
        print("The area of {} is {}".format(shape.upper(), round(table[shape][index], 2)))
        print(pageBreak)

main()