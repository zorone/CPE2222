from tkinter import *
from tkinter import ttk

class Main(Tk):
    def __init__(self):
        self.geometry("270x165")
        self.title('Canvas Drawing')
        
        self.mainFrameOption = {
            'config': {
                
            },
            'position': {
                'x': 0,
                'y': 0,
                'width': 1,
                'height': 2,
                'sticky': (N,E,W,S)
            }
        }
        self.mainFrame = self.buildFrame(self, self.mainFrameOption)
        
    def buildFrame(self, root, **options):
        if options['config'].get('padding') == None:
            options['config']['padding'] = 5

        res = ttk.Frame(
            root,
            padding = options['config']['padding'])
        res.grid(
            row = options['pos']['x'],
            column = options['pos']['y']
        )
        return res
        
    def buildLabelFrame(self, root, text, **options):
        if options['config'].get('padding') == None:
            options['config']['padding'] = 5

        res = ttk.LabelFrame(
            root,
            padding = options['config']['padding'],
            text = text)
        res.grid()
        return res

if __name__ == '__main__':
    main = Main()
    main.mainloop()