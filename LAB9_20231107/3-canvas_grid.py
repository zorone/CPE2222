from tkinter import *
from tkinter import ttk

class Main(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("270x165")
        self.title('Canvas Drawing')
        
        '''
        self.mainFrameOption = {
            'config': {
                
            },
            'pos': {
                'x': 0,
                'y': 0,
                'width': 1,
                'height': 2,
                'sticky': (N,E,W,S)
            }
        }
        self.mainFrame = self.buildFrame(self, self.mainFrameOption)
        '''
        self.labelFrameOption = {
            'config': {
                'padding': 5
            },
            'pos': {
                'x': 0,
                'y': 0,
                'width': 1,
                'height': 1,
                'sticky': (N,E,W,S)
            }
        }
        self.labelFrame = self.buildLabelFrame(self, "Drawing Setting", self.labelFrameOption)
        
    def buildFrame(self, root, options):
        if options['config'].get('padding') == None:
            options['config']['padding'] = 5

        res = ttk.Frame(
            root,
            padding = options['config']['padding'])
        res.grid(
            column = options['pos']['x'],
            columnspan = options['pos']['width'],
            row = options['pos']['y'],
            rowspan = options['pos']['height'],
            sticky = options['pos']['sticky']
        )
        return res
        
    def buildLabelFrame(self, root, text, options):
        if options['config'].get('padding') == None:
            options['config']['padding'] = 5

        res = ttk.LabelFrame(
            root,
            padding = options['config']['padding'],
            text = text)
        res.grid(
            column = options['pos']['x'],
            columnspan = options['pos']['width'],
            row = options['pos']['y'],
            rowspan = options['pos']['height'],
            sticky = options['pos']['sticky']
        )
        return res

if __name__ == '__main__':
    main = Main()
    main.mainloop()