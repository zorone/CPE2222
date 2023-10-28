# https://stackoverflow.com/q/31606881

from Tkinter import *

def toplevelwin():

    def clear():
        return

    def select():
        return

    def unselect():
        return

    def done():
        return

    def enter():
        return

    window = Toplevel()

    frame0 = Frame(window)
    frame0.grid(row=0, column=0, sticky=W, padx=5, pady=5, columnspan=2)
    frame0.grid_columnconfigure(1,weight=2)
    lblentry = Label(frame0, text="Entery Box:")
    lblentry.grid(row=0, column=0, sticky=W)
    entrybx = Entry(frame0)
    entrybx.grid(row=1,column=0,sticky=N+S+E+W, columnspan=2)
    entrybt = Button(frame0, text=' Enter ', command=enter)
    entrybt.grid(row=1,column=2,sticky=N+W, padx=3)

    frame1 = Frame(window)
    frame1.grid(row=1, column=0, sticky=E+W, padx=5, pady=5)
    lblshow_lst = Label(frame1, text="List Box 1:")
    lblshow_lst.grid(row=0,sticky=W)
    show_lst = Listbox(frame1)
    show_lst.grid(row=1,sticky=W)

    frame2 = Frame(window)
    frame2.grid(row=1, column=1, sticky=W)
    frame2.grid_columnconfigure(1,weight=1)
    selbtn = Button(frame2, text='Select', command=select)
    selbtn.grid(row=0, padx=5, sticky=E+W)
    selbtn.grid_columnconfigure(1,weight=1)
    uselbtn = Button(frame2, text='Unselect', command=unselect)
    uselbtn.grid(row=1, padx=5, sticky=E+W)
    uselbtn.grid_columnconfigure(1,weight=1)

    frame3 = Frame(window)
    frame3.grid(row=1, column=2, sticky=W, padx=5, pady=5)
    lblsel_lst = Label(frame3, text="List Box 2:")
    lblsel_lst.grid(row=0,sticky=W)
    sel_lst = Listbox(frame3)
    sel_lst.grid(row=1, column=0, sticky=W)

    frame4 = Frame(window)
    frame4.grid(row=2, column=0, sticky=E, padx=5, pady=5)
    Button(frame4, text=' Done ', command=done).grid(row=0, column=0, padx=7 ,pady=2)
    Button(frame4, text='Clear', command=clear).grid(row=0,column=1, padx=7,pady=2)
    window.wait_window(window)


root = Tk()
toplevelwin()
root.mainloop()