import os

class Main():
    def __init__(self):
        try:
            path = os.listdir()
            print(path)
                
        except OSError:
            print("Incorrect file Structure, please check if your workspace has all files that is needed.")

if __name__ == '__main__':
    main = Main()