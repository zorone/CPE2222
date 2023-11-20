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
            
            student = list()
            instructor = list()
            CVE = list()
            IND = list()
            CPE = list()
            
            F = open("input.txt", 'r', encoding='utf-8')
            F.readline()
                
        except OSError:
            print("Incorrect file Structure, please check if your workspace has all files that is needed.")

if __name__ == '__main__':
    main = Main()