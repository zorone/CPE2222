# https://stackoverflow.com/a/76203660

import tkinter as tk
import tkinter.ttk as ttk
from functools import partial


# Create class to store all GUI Styles
class GuiStyles:
    # In __init__ method add an argument to set which window to style
    def __init__(self, window_to_style):

        # Add desired styles but instead of 'self' we will be styling the window
        # passed in the argument
        window_to_style.configure(background='white')
        window_to_style.option_add('*Font', 'Helvetica 12 bold')
        window_to_style.option_add('*foreground', 'black')
        window_to_style.option_add('*background', 'white')

        window_to_style.style = ttk.Style()
        window_to_style.style.theme_use('default')
        window_to_style.style.map('T.TButton',
                                  background=[('active', 'pressed', 'red'),
                                              ('!active', 'light blue'),
                                              ('active', '!pressed', 'pink')])
        window_to_style.style.configure('R.TLabel',
                                        font=('helvetica', '12'),
                                        foreground='Green',
                                        background='white')


class GUI3(tk.Toplevel):
    def __init__(self):
        super().__init__()

        # Any window-specific configurations
        self.title("Gui3")
        self.geometry('200x200')

        # Create an instance of 'GuiStyles' class and add 'self' as an argument
        GuiStyles(window_to_style=self)
        # Still have to create 'self.style' or else we get an error
        self.style = ttk.Style()

        # Add widgets with styles defined in 'GuiStyles'
        self.btn_sel = ttk.Button(self,
                                  text='FINAL GUI',
                                  width=17,
                                  style='T.TButton',
                                  command=None)
        self.btn_sel.place(x=100, y=100, anchor="center")


class GUI2(tk.Toplevel):
    def __init__(self):  # Special Method, first argument is self.
        super().__init__()

        self.geometry('200x200')
        self.title("Gui2")

        GuiStyles(window_to_style=self)
        self.style = ttk.Style

        # We can add window-specific styles to rewrite anything that we want
        # from the 'GuiStyles' class
        self.option_add('*Font', 'Helvetica 11')

        self.lbl_example = ttk.Label(self,
                                     text='Example Label',
                                     style='R.TLabel')
        self.lbl_example.place(x=100, y=60, anchor="center")

        self.btn_sel = ttk.Button(self,
                                  text='Open Gui3',
                                  width=17,
                                  style='T.TButton',
                                  command=partial(self.open_gui_3))
        self.btn_sel.place(x=100, y=100, anchor="center")

    def open_gui_3(self):
        mine = GUI3()
        mine.grab_set()


class Main(tk.Tk):
    def __init__(self, ):
        super().__init__()

        GuiStyles(window_to_style=self)
        self.style = ttk.Style()

        self.title("Main Window")
        self.geometry('300x200')

        self.lbl_example = ttk.Label(self,
                                     text='Example Label',
                                     style='R.TLabel')

        self.lbl_example.place(x=150, y=60, anchor="center")

        self.btn_dio = ttk.Button(self,
                                  text='Open Gui2',
                                  style='T.TButton',
                                  command=partial(self.open_giu_2))
        self.btn_dio.place(x=150, y=100, anchor="center")

    def open_giu_2(self):
        dio = GUI2()
        dio.grab_set()


if __name__ == "__main__":
    main = Main()
    main.mainloop()