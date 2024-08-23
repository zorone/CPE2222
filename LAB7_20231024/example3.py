# https://stackoverflow.com/questions/76202930/python-classes-using-ttk-style-in-multiple-classes-using-tk-toplevel

import configparser                                     # parsing multiple GUI's
import datetime as dt                                   # Date library
import time                                             # call time to count/pause
import tkinter as tk                                    # Tkinter's Tk class
import tkinter.ttk as ttk                               # Tkinter's Tkk class

from functools import partial                           # freezing one function while executing another
from PIL import ImageTk, Image                          # Displaying LAL background photo
from python_imagesearch.imagesearch import imagesearch  # opening images, pip package
from tkinter import messagebox                          # Exit standard message box

config = configparser.ConfigParser()
samp_arr = []              # initalize all global variables and global arrays to call between classes
btn_pres_cnt = 1            # setting count to 0 to be able to call it a global variable within the function

##########################################################################################################################################
#################################################      MINESWEEP BUTTONS         #########################################################
##########################################################################################################################################
class GUI3(tk.Toplevel):
    def __init__(self):  # Special Method, first argument is self.
        super().__init__()

        self.title("Sample Numbers")
        self.geometry('450x450')
        self.configure(background='white')              # Set background color
        self.option_add('*Font', 'Helvetica 11')        # set the font and size for entire Dioptics
        self.option_add('*foreground', 'black')         # set the text color, hex works too '#FFFFFF'
        self.option_add('*background', 'white')         # set the background to white

        #################################################     TTK BUTTON & LABEL STYLE         ################################################
        self.style = ttk.Style(self)
        self.style.theme_use('default')  # alt, default, clam and classic

        self.style.map('T.TButton', background=[('active', 'pressed', 'white'), ('!active', 'white'),('active', '!pressed', 'grey')])  # active, not active, not pressed
        self.style.map('T.TButton', relief=[('pressed', 'sunken'), ('!pressed', 'raised')])  # pressed, not pressed
        self.style.configure('T.TButton', font=('Helvetica', '10'))

        self.style.map('B.TButton', background=[('active', 'pressed', 'white'), ('!active', 'white'), ('active', '!pressed', 'grey')])  # Press me Button always hot pink when pressed
        self.style.map('B.TButton', relief=[('pressed', 'sunken'), ('!pressed', 'raised')])  # pressed, not pressed
        self.style.configure('B.TButton', font=('helvetica', '12', 'bold'))

        self.style.map('P.TButton', background=[('active', 'pressed', '#FF69B4'), ('!active', 'white'), ('active', '!pressed', 'grey')])  # Press me Button always hot pink when pressed
        self.style.map('P.TButton', relief=[('pressed', 'sunken'), ('!pressed', 'raised')])  # pressed, not pressed
        self.style.configure('P.TButton', font=('helvetica', '12', 'bold'))

        self.style.configure('R.TLabel', font=('helvetica', '12'), foreground='black', background='white')
        self.style.configure('B.TLabel', font=('helvetica', '12', 'bold'), foreground='black', background='white')

        ################################################                 MAIN BODY                ################################################
        counter = 0
        btn_text = (
            '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
            '20',
            '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38',
            '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56',
            '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74',
            '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92',
            '93', '94', '95', '96', '97', '98', '99', '100')
        btn_ids = []

        def get_samp(n):
            btn_name = (btn_ids[n])  # create 100 unique button names from btn_ids[n]
            btn_name.config(text=f"{btn_text[n]}")  # configure the string of button numbers to the buttons
            print("button name: ", btn_name)  # btn_name = .!window.!button##
            samp_arr.append(n + 1)  # add n+1 button click to list
            dis_RT(self)

        lbl_samp = ttk.Label(self, text=' ', style = 'R.TLabel', wraplength=330, justify='left')
        lbl_samp.place(x=110, y=335, anchor='w')
        lbl_samp_nums = ttk.Label(self, text="Sample #'s: ", wraplength=120, style='B.TLabel').place(x=10, y=325)
        def dis_RT(self):
            print("samp_arr: ", ', '.join(map(str, samp_arr)))
            lbl_samp.config(text=', '.join(map(str, samp_arr)))

        def clear():
            samp_arr.clear()
            lbl_samp.config(text=' ')
            print("List after .clear() ", samp_arr)

        def save():
            print("This button is uselss, but makes people feel safe.")
            self.destroy()

        def exit():
            print("Clear and close.")
            clear()
            self.destroy()

        for r in range(10):
            for c in range(10):
                print(counter, r, c)
                btn_grid = ttk.Button(self, width=4, text=btn_text[counter], style='T.TButton', command=partial(get_samp, counter))  # create buttons & assign unique arg (i) to run function (change)
                # btn_grid.bind('<Button 1>', write_samp)
                btn_grid.grid(row=r, column=c)
                btn_ids.append(btn_grid)  # add ID to list
                counter += 1  # update counter for next button text

        self.btn_clr = ttk.Button(self, text='Clear All', width=5, style='T.TButton', command=partial(clear))
        self.btn_clr.bind('<Button-1>', self.pink)            # class.function(instance)
        self.btn_clr.place(x=50, y=400)

        self.btn_save = ttk.Button(self, text='Save & Close', width=12, style='T.TButton', command=partial(save))
        self.btn_save.bind('<Button-1>', self.pink)            # class.function(instance)
        self.btn_save.place(x=160, y=400)

        self.btn_exit = ttk.Button(self, text='Exit without Saving', width=17, style='T.TButton', command=partial(exit))
        self.btn_save.bind('<Button-1>', self.pink)            # class.function(instance)
        self.btn_exit.place(x=310, y=400)

    def pink(self, event):
        global btn_pres_cnt  # initializing btn_pres_cnt as a global varaible so that it adds through every iteration
        if (
                btn_pres_cnt == 5 or btn_pres_cnt == 10 or btn_pres_cnt == 15 or btn_pres_cnt == 20 or btn_pres_cnt == 25):  # button turns pink when btn_pres_cnt=100, and =200 and = 300.
            self.style.map('T.TButton', background=[('active', 'pressed', '#FF69B4'), ('!active', 'white'), ('active', '!pressed', 'grey')])  # only the button being pressed turns hot pink
            self.style.configure('T.Button', font=('Helvetica', '12', 'bold'))
        else:  # else is the normal style
            self.style.map('T.TButton',background=[('active', 'pressed', 'white'), ('!active', 'white'), ('active', '!pressed', 'grey')])
            self.style.configure('T.Button', font=('Helvetica', '12', 'bold'))
        print('btn_pres_cnt = ', btn_pres_cnt)
        btn_pres_cnt += 1                                       # This is always executed at the end of the if else

##########################################################################################################################################
############################################        END MINESWEEP POP UP WINDOWS        ##################################################
##########################################################################################################################################
###############################################          Sample Input & Size       #######################################################
##########################################################################################################################################

class GUI2(tk.Toplevel):
    def __init__(self):  # Special Method, first argument is self.
        super().__init__()

        self.geometry('810x275')
        self.title("Sample Sizes")                      # title might have to be main window, from the last statement; if __name__ == "__main__":
        self.configure(background='white')              # Set background color

        self.option_add('*Font', 'Helvetica 11')        # set the font and size for entire GUI2
        self.option_add('*foreground', 'black')         # set the text color, hex works too '#FFFFFF'
        self.option_add('*background', 'white')         # set the background to white

        #################################################    TKK BUTTON & LABEL STYLE    ################################################
        self.style = ttk.Style()
        self.style.theme_use('default')  # alt, default, clam and classic
        
        self.style.map('T.TButton', background=[('active', 'pressed', 'white'), ('!active', 'white'), ('active', '!pressed', 'grey')])             # active, not active, not pressed
        self.style.map('T.TButton', relief=[('pressed', 'sunken'), ('!pressed', 'raised')])  # pressed, not pressed
        self.style.configure('T.TButton', font=('Helvetica', '10'))
        
        self.style.map('B.TButton', background=[('active', 'pressed', 'white'), ('!active', 'white'),('active', '!pressed', 'grey')])             # Press me Button always hot pink when pressed
        self.style.map('B.TButton', relief=[('pressed', 'sunken'), ('!pressed', 'raised')])  # pressed, not pressed
        self.style.configure('B.TButton', font=('helvetica', '12', 'bold'))
        
        self.style.map('P.TButton', background=[('active', 'pressed', '#FF69B4'), ('!active', 'white'),('active', '!pressed', 'grey')])             # Press me Button always hot pink when pressed
        self.style.map('P.TButton', relief=[('pressed', 'sunken'), ('!pressed', 'raised')])  # pressed, not pressed
        self.style.configure('P.TButton', font=('helvetica', '12', 'bold'))
        
        self.style.configure('B.TLabel', font=('helvetica', '12', 'bold'), foreground='black', background='white')
        self.style.configure('R.TLabel', font=('helvetica', '12'), foreground='black', background='white')

        #####################################                   MAIN BODY                ################################################
        self.lbl_cmd_mc1 = ttk.Label(self, text="Are the samples numbered in order?", style='B.TLabel')
        self.lbl_cmd_mc1.place(x=150, y=20, anchor='center')
        self.lbl_cmd_mc2 = ttk.Label(self, text="If not, click 'Manual' and a new window", style='B.TLabel')
        self.lbl_cmd_mc2.place(x=150, y=40, anchor='center')
        self.lbl_cmd_mc3 = ttk.Label(self, text="will popup to manually select the sample", style='B.TLabel')
        self.lbl_cmd_mc3.place(x=150, y=60, anchor='center')
        self.lbl_cmd_mc4 = ttk.Label(self, text="numbers listed in the work order.", style='B.TLabel')
        self.lbl_cmd_mc4.place(x=150, y=80, anchor='center')

        self.lbl_samp_nums = ttk.Label(self, text="Sample #'s: ", style='B.TLabel')     # top right, displays samples
        self.lbl_samp_nums.place(x=300, y=50)

        self.lbl_cmd_s1 = ttk.Label(self, text="# of Samples: ", style='B.TLabel')      # middle left, asking for user entry
        self.lbl_cmd_s1.place(x=20, y=140)

        GUI2.entry_s1 = tk.Entry(self, width=10)                                        # get entry_s1, pass to main gui
        GUI2.entry_s1.focus_set()                                                       # Places cursor in the first entry box.
        GUI2.entry_s1.place(x=130, y=140)

        self.lbl_cmd_dd = ttk.Label(self, text="Size:", style='B.TLabel')
        self.lbl_cmd_dd.place(x=340, y=150, anchor='center')

        self.btn_sel = ttk.Button(self, text='Select Sample #s', width=17, style='T.TButton', command=partial(self.open_mine))
        self.btn_sel.bind('<Button-1>', self.pink)           
        self.btn_sel.place(x=20, y=220)

        self.btn_dis = ttk.Button(self, text='Display', width = 8, style='T.TButton', command=partial(self.display))
        self.btn_dis.bind('<Button-1>', self.pink)  
        self.btn_dis.place(x=170, y=220)

        self.btn_clr = ttk.Button(self, text='Clear All', width = 9, style='T.TButton', command=partial(self.clear))
        self.btn_clr.bind('<Button-1>', self.pink)  
        self.btn_clr.place(x=260, y=220)

        self.btn_save = ttk.Button(self, text='Save & Close', width = 14, style='T.TButton' ,command=partial(self.save))
        self.btn_save.bind('<Button-1>', self.pink)  
        self.btn_save.place(x=520, y=220)

        self.btn_exit = ttk.Button(self, text='Exit Without Saving', width = 17, style='T.TButton', command=partial(self.exit))
        self.btn_exit.bind('<Button-1>', self.pink)  
        self.btn_exit.place(x=650, y=220)

        self.drp_dn_opt = [  # Dropdown menu options
            "4", "4.5", "5", "5.5", "6", "6.5", "7", "7.5", "8", "8.5", "9", "9.5", "10", "10.5", "11", "11.5", 
            "12", "12.5", "13", "13.5", "14", "14.5", "15", "15.5", "16", "16.5", "17", "17.5", "18", "18.5",
            "19", "19.5", "20", "20.5", "21", "21.5", "22", "22.5", "23", "23.5", "24", "24.5", "25", "25.5", 
            "26", "26.5", "27", "27.5", "28", "28.5", "29", "29.5", "30"]

        GUI2.dio_sz = tk.StringVar()      # datatype of menu text
        GUI2.dio_sz.trace('w', self.dio())
        GUI2.dio_sz.set("Select Size")    # initial menu text

        self.drp_dn_wdt = len(max(self.drp_dn_opt, key=len))

        self.drop = tk.OptionMenu(self, GUI2.dio_sz, *self.drp_dn_opt)  # Create Dropdown menu
        self.drop.config(width=14)
        self.drop.place(x=410, y=135)

    def open_mine(self):
        mine = GUI3()
        mine.grab_set()

    def dio(self):
        self.lbl_out_d = ttk.Label(self, textvariable=GUI2.dio_sz, style='B.TLabel')
        self.lbl_out_d.place(x=450, y=200, anchor='center')
        print(f"The size is: ", GUI2.dio_sz)
        GUI2.dioptic = GUI2.dio_sz

    def display(self):  # when the save button is selected in minesweep, it writes to this GUI screen
        samp_arr.sort(reverse=False)  # sort in ascending order.
        if samp_arr is True:
            self.lbl_sam = ttk.Label(self, text=', '.join(map(str, samp_arr)), style = 'R.TLabel', wraplength=400, justify='left')
            self.lbl_sam.place(x=410, y=52, anchor='w')
            print(f"The array is: ", ', '.join(map(str, samp_arr)))
        else:
            self.lbl_sam = ttk.Label(self, text= "1-" + GUI2.entry_s1.get(), style = 'R.TLabel', wraplength=400, justify='left')
            self.lbl_sam.place(x=410, y=52, anchor='w')
            print(f"The entry is: 1-", GUI2.entry_s1.get())
            GUI2.entry_s1 = GUI2.entry_s1.get()

    def clear(self):            # Need a way to delete/clear/erase/reset label display lbl_sam in display function.
        samp_arr.clear()
        self.lbl_sam.config(text=' ')
        print("List after .clear() ", samp_arr)

    def save(self):
        print("We don't actually use this. It just makes people feel safe.")
        self.destroy()

    def exit(self):
        print("Close without saving, clear array. ")
        samp_arr.clear()
        self.destroy()

    def pink(self, event):
        global btn_pres_cnt  # initializing btn_pres_cnt as a global varaible so that it adds through every iteration
        if (
                btn_pres_cnt == 5 or btn_pres_cnt == 10 or btn_pres_cnt == 15 or btn_pres_cnt == 20 or btn_pres_cnt == 25):  # button turns pink when btn_pres_cnt=100, and =200 and = 300.
            self.style.map('T.TButton', background=[('active', 'pressed', '#FF69B4'), ('!active', 'white'), (
            'active', '!pressed', 'grey')])  # only the button being pressed turns hot pink
            self.style.configure('T.Button', font=('Helvetica', '12', 'bold'))
        else:  # else is the normal style
            self.style.map('T.TButton',
                        background=[('active', 'pressed', 'white'), ('!active', 'white'), ('active', '!pressed', 'grey')])
            self.style.configure('T.Button', font=('Helvetica', '12', 'bold'))
        print('btn_pres_cnt = ', btn_pres_cnt)
        btn_pres_cnt += 1                                       # This is always executed at the end of the if else

##########################################################################################################################################
#################################################         1st  MAIN  SCREEN              #################################################
##########################################################################################################################################
#################################################      INITIALIZING STANDARD DISPLAY     #################################################
##########################################################################################################################################

class Main(tk.Tk):
    def __init__(self):  # Special Method, first argument is self.
        super().__init__()

        self.geometry('1300x820')                         # Set the geometry of Tkinter frame
        self.title("Main Window")
        self.configure(background='white')               # Set background color
        self.option_add('*Font', 'Helvetica 12 bold')    # set the font and size for entire self
        self.option_add('*foreground', 'black')          # set the text color, hex works too '#FFFFFF'
        self.option_add('*background', 'white')          # set the background to white

        #################################################    TKK BUTTON & LABEL STYLE    ################################################
        self.style = ttk.Style()
        self.style.theme_use('default')  # alt, default, clam and classic
        
        self.style.map('T.TButton', background=[('active', 'pressed', 'white'), ('!active', 'white'), ('active', '!pressed', 'grey')])             # active, not active, not pressed
        self.style.map('T.TButton', relief=[('pressed', 'sunken'), ('!pressed', 'raised')])  # pressed, not pressed
        self.style.configure('T.TButton', font=('Helvetica', '10'))
        
        self.style.map('B.TButton', background=[('active', 'pressed', 'white'), ('!active', 'white'),('active', '!pressed', 'grey')])             # Press me Button always hot pink when pressed
        self.style.map('B.TButton', relief=[('pressed', 'sunken'), ('!pressed', 'raised')])  # pressed, not pressed
        self.style.configure('B.TButton', font=('helvetica', '12', 'bold'))
        
        self.style.map('P.TButton', background=[('active', 'pressed', '#FF69B4'), ('!active', 'white'),('active', '!pressed', 'grey')])             # Press me Button always hot pink when pressed
        self.style.map('P.TButton', relief=[('pressed', 'sunken'), ('!pressed', 'raised')])  # pressed, not pressed
        self.style.configure('P.TButton', font=('helvetica', '12', 'bold'))
        
        self.style.configure('B.TLabel', font=('helvetica', '12', 'bold'), foreground='black', background='white')
        self.style.configure('R.TLabel', font=('helvetica', '10'), foreground='black', background='white')

        ################################################                 MAIN BODY                ################################################
        # Display the command label before the entry box to indicate what information the Opterator is to type
        lbl_cmd_date = ttk.Label(self, text="Todays Date is:", style='B.TLabel').place(x=50, y=25)
        lbl_cmd_cred = ttk.Label(self, text="Enter Operator Credentials:", style='B.TLabel').place(x=50, y=175)
        lbl_cmd_WO = ttk.Label(self, text="Enter Work Order Number:", style='B.TLabel').place(x=50, y=225)
        lbl_cmd_samp = ttk.Label(self, text="Enter Sample Sizes:", style='B.TLabel').place(x=50, y=275)
        lbl_cmd_meas = ttk.Label(self, text="Select Measurement Size:", style='B.TLabel').place(x=50, y=325)

        # Entry boxes to take information from operator
        self.entry_cred = ttk.Entry(self, width=10)
        self.entry_cred.focus_set()                                          # Places cursor in the first entry box.
        self.entry_cred.place(x=300, y=175)
        self.entry_WO = ttk.Entry(self, width=20)
        self.entry_WO.place(x=300, y=225)

        # Display the label of what user input as an output
        lbl_disp_cred = ttk.Label(self, text="Credentials:", style='B.TLabel').place(x=50, y=520)
        lbl_disp_WO = ttk.Label(self, text="Work Order Number:", style='B.TLabel').place(x=50, y=560)
        lbl_disp_samp = ttk.Label(self, text="Size :", style='B.TLabel').place(x=50, y=600)
        lbl_disp_dio = ttk.Label(self, text="Samples #s:", style='B.TLabel').place(x=50, y=640)

        # Display the user inputs as outputs
        self.lbl_out_date = ttk.Label(self, text=f'{dt.datetime.now():%b %d, %Y}', style='B.TLabel').place(x=300, y=25)
        self.lbl_out_cred = ttk.Label(self, text='', style='R.TLabel', width=4)
        self.lbl_out_cred.place(x=300, y=520)
        self.lbl_out_WO = ttk.Label(self, text='', style='R.TLabel', width=15)
        self.lbl_out_WO.place(x=300, y=560)
        
        #################################################        BUTTONS TO BE CLICKED         ################################################
        self.btn_dio = ttk.Button(self, text='Select Samples',style='T.TButton', command=partial(self.open_dio))            # Open new self for dioptic entry and sample sizes
        self.btn_dio.bind('<Button-1>', self.pink)
        self.btn_dio.place(x=300, y=272)

        self.btn_exit = ttk.Button(self, text='Close', width = 12, style='B.TButton', command=partial(self.exit))
        self.btn_exit.bind('<Button-1>', self.pink)
        self.btn_exit.place(x=1150, y=720)

    # Display user inputs as outputs
    def cred(self):
        cred = self.entry_cred.get()[:3]                                 # entry_cred is the variable we are passing. Limit 3 characters
        self.lbl_out_cred.configure(text=cred)                           # Display cred entry from user on self
        self.ws.cell(column=1, row=self.new_line, value=cred)         
        print("entry_cred: ", cred)                                

    def WO(self):
        WO = self.entry_WO.get()[:13]                                     # entry_WO is the variable we are passing. Limit 10 characters
        self.lbl_out_WO.configure(text=WO)                                # Display WO entry from user on self
        self.ws.cell(column=2, row=self.new_line, value=WO)   
        print("entry_wo: ", WO)

    def display(self):  # when the save button is selected in minesweep, it writes to this GUI screen
        dio_sz = GUI2.dioptic
        self.lbl_dio = ttk.Label(self, textvariable=dio_sz, style='R.TLabel', justify='left')
        self.lbl_dio.place(x=310, y=600, anchor='center')
        self.ws.cell(column=3, row=self.new_line, value=dio_sz.get()) 
        print(f"The dioptic size is: ", dio_sz)

        samp_arr.sort(reverse=False)  # sort in ascending order.
        if samp_arr is True:
            self.lbl_sam = ttk.Label(self, text=', '.join(map(str, samp_arr)), style = 'R.TLabel', wraplength=400, justify='left')
            self.lbl_sam.place(x=300, y=640, anchor='w')
            print(f"The array is: ", ', '.join(map(str, samp_arr)))
        else:
            self.lbl_sam = ttk.Label(self, text= "1 - " + GUI2.entry_s1, style = 'R.TLabel', wraplength=400, justify='left')
            self.lbl_sam.place(x=300, y=640, anchor='w')
            print(f"The entry is: 1-", GUI2.entry_s1)

    def exit(self):
        msg_box = tk.messagebox.askquestion('Exit', 'Are you sure you want to exit the application?', icon='warning')
        if msg_box == 'yes':
            self.destroy()
        else:
            tk.messagebox.showinfo('Exit', "Thanks for staying, please continue.")

    def pink(self, event):
        global btn_pres_cnt  # initializing btn_pres_cnt as a global varaible so that it adds through every iteration
        if (
                btn_pres_cnt == 5 or btn_pres_cnt == 10 or btn_pres_cnt == 15 or btn_pres_cnt == 20 or btn_pres_cnt == 25):  # button turns pink when btn_pres_cnt=100, and =200 and = 300.
            self.style.map('T.TButton', background=[('active', 'pressed', '#FF69B4'), ('!active', 'white'), ('active', '!pressed', 'grey')])  # only the button being pressed turns hot pink
            self.style.configure('T.Button', font=('Helvetica', '12', 'bold'))
        else:  # else is the normal style
            self.style.map('T.TButton',background=[('active', 'pressed', 'white'), ('!active', 'white'), ('active', '!pressed', 'grey')])
            self.style.configure('T.Button', font=('Helvetica', '12', 'bold'))
        print('btn_pres_cnt = ', btn_pres_cnt)
        btn_pres_cnt += 1                                       # This is always executed at the end of the if else

    def open_dio(self):
        dio = GUI2()
        dio.grab_set()
    
# Must be at the end of the program in order for the application to run b/c windows is constantly updating
if __name__ == "__main__":
    main = Main()
    main.mainloop()