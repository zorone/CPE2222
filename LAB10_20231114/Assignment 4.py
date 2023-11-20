import os

class Main():
    def __init__(self):
        try:
            path = os.path.dirname(os.path.abspath(__file__))
            print(path)
                
        except OSError:
            print("Incorrect file Structure, please check if your workspace has all files that is needed.")

if __name__ == '__main__':
    main = Main()