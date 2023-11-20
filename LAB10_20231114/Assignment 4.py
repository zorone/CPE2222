import os

class Main():
    def __init__(self):
        try:
            path = os.path.dirname(os.path.abspath(__file__))
            os.chdir(path)
            path = os.listdir()
            if "readme.txt" not in path:
                raise OSError
            if "input.txt" not in path:
                raise OSError
            
            structure = {"นักศึกษา": {"นักศึกษา": "นักศึกษา"},
                         "อาจารย์": {"อาจารย์": "คณาจารย์", "โยธา": "โยธา", "อุตสาหการ": "อุตสาหการ", "คอมพิวเตอร์": "คอมพิวเตอร์"}}
            
            route(structure)
                
        except OSError:
            print("Incorrect file Structure, please check if your workspace has all files that is needed.")

def route(r):
    key = r.keys()
    
    for k in key:
        if type(r[k]) == type(dict()):
            route(r[k])

if __name__ == '__main__':
    main = Main()