print("                Basic math formulas               ")
print("##################################################")

print("                Area of Triangle                  ")
print("--------------------------------------------------")
b = input("Enter Base:")
b = float(b)
h = input("Enter Height:")
h = float(h)
A = (1/2)*b*h
print("The area is {}".format(A))
print("--------------------------------------------------")

print("                Area of Rectangle                 ")
print("--------------------------------------------------")
l = input("Enter Length:")
l = float(l)
w = input("Enter Width:")
w = float(w)
A = l*w
print("The area is {}".format(A))
print("--------------------------------------------------")

print("        The Longest Size of Right Triangle        ")
a = input("Enter length of the 1st side:")
a = float(a)
b = input("Enter length of the 2nd side:")
b = float(b)
l = (a**2 + b**2)**(1/2)
print("The length of the longest side is {}".format(l))
print("--------------------------------------------------")

print("        The Solution of Quadratic Formula         ")
c = input("Enter Constant (\"c\"):")
c = float(c)
b = input("Enter Coefficient of Linear Term(\"b\"):")
b = float(b)
a = input("Enter Coefficient of Quadratic Term(\"a\"):")
a = float(a)
x = ((-1)*b + (b**2 - 4*a*c)**(1/2))/(2*a)
print("The 1st solution is x = {}".format(x))
x = ((-1)*b - (b**2 - 4*a*c)**(1/2))/(2*a)
print("The 2nd solution is x = {}".format(x))
print("--------------------------------------------------")

print("                Distance of 2 points              ")
x1 = input("Enter x of the 1st point:")
x1 = float(x1)
y1 = input("Enter y of the 1st point:")
y1 = float(y1)
x2 = input("Enter x of the 2nd point:")
x2 = float(x2)
y2 = input("Enter y of the 2nd point:")
y2 = float(y2)
d = ((y2 - y1)**2 + (x2 - x1)**2)**(1/2)
print("The distance is {}".format(d))
print("--------------------------------------------------")