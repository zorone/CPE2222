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
            data = F.readlines()
            tempLock = False
            tempSkip = False
            nameType = list()
            tempName = ''
            buffer = ''
            
            for s in data:
                if not tempLock:
                    tempName = s
                    tempLock = True
                    continue
                
                if not tempSkip:
                    if len(nameType) > 1:
                        nameType.clear()
                        tempSkip = True
                        continue
                    if "นักศึกษา" in s:
                        student += [s]
                        tempSkip = True
                        continue
                    if "อาจารย์" in s:
                        instructor += [s]
                        nameType += ["instructor"]
                        continue
                    if "โยธา" in s:
                        CVE += [s]
                        nameType += ["CVE"]
                        continue
                    if "อุตสาหการ" in s:
                        IND += [s]
                        nameType += ["IND"]
                        continue
                    if "คอมพิวเตอร์" in s:
                        CPE += [s]
                        nameType += ["CPE"]
                        continue
                    
                if s == '\n':
                    tempLock = False
                    tempSkip = False

        except OSError:
            print("Incorrect file Structure, please check if your workspace has all files that is needed.")

if __name__ == '__main__':
    main = Main()