import os

class Main():
    def __init__(self):
        try:
            path = os.path.dirname(os.path.abspath(__file__))
            path = os.listdir(path)
            if "readme.txt" not in path:
                raise OSError
            if "input.txt" not in path:
                raise OSError
            
            structure = {"นักศึกษา": "นักศึกษา", "อาจารย์": ["คณาจารย์", "โยธา", "อุตสาหการ", "คอมพิวเตอร์"]}
            
            for route in structure:
                
                
        except OSError:
            print("Incorrect file Structure, please check if your workspace has all files that is needed.")

if __name__ == '__main__':
    main = Main()