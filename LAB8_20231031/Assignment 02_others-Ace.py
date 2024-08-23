from tkinter import *

def c():
    s = r.get()
    s1 = l.get()
    s2 = w.get()

    if(s1 == '' or s2 == ''): # check for null character
        s1 = 0
        s2 = 0
    else:
        s1 = float(s1)
        s2 = float(s2)

    if s == 1:  # Area of Rectangle
        e1 = s1 * s2
        e2.config(text=f"The area of rectangle with length of {s1} and width of {s2} is {e1}")
    elif s == 2:  # Area of Triangle
        e1 = 0.5 * s1 * s2
        e2.config(text=f"The aarea of triangle with base of {s1} and height of {s2} is {e1}")
        l1.config(text=f"Base:")
        w1.config(text=f"Height:")
        c1.config(text=f"Area")
    elif s == 3:  # Pythagorean
        e1 = (s1 * 2 +s2 * 2) ** 0.5
        e2.config(text=f"The longest size of right triangle({s1},{s2}) is {e1}")
        l1.config(text=f"The 1st size:")
        w1.config(text=f"The 2st size:")
        c1.config(text=f"Pythagorean Theory")

def text():
    s = r.get()
    if s == 1:
        l1.config(text=f"Length:")
        w1.config(text=f"width:")
        c1.config(text=f"Area")

root = Tk()
root.title("CPE2222")
root.geometry("400x200")

L = Label(root, text=" "*2)
L.grid(row=0, column=0)
L1 = Label(root, text=" "*5)
L1.grid(row=1, column=0)
L2 = Label(root, text=" "*5)
L2.grid(row=1, column=2)

a1 = LabelFrame(root, text="Calculation", padx=10, pady=10)
a1.grid(row=1, column=1)

r = IntVar()
r.set(3)

r1 = Radiobutton(a1, text="Area of Rectangle", variable=r, value=1, command=text)
r1.grid(row=0, column=0)

r2 = Radiobutton(a1, text="Area of Triangle   ", variable=r, value=2)
r2.grid(row=1, column=0)

r3 = Radiobutton(a1, text="Pyhagorean          ", variable=r, value=3)
r3.grid(row=2, column=0)

a2 = LabelFrame(root, text="Parameter Setting", padx=10, pady=10)
a2.grid(row=1, column=3)

l1 = Label(a2, text="")
l1.grid(row=0, column=1)
l = Spinbox(a2)
l.grid(row=0, column=2)

w1 = Label(a2, text="")
w1.grid(row=1, column=1)
w = Spinbox(a2)
w.grid(row=1, column=2)

c1 = Button(a2, text="", command=c)
c1.grid(row=6, column=0, columnspan=3)

e2 = Label(root, text="", justify='center')
e2.grid(row=2, column=1, columnspan=3, sticky=(N,S,E,W))

c()
root.mainloop()