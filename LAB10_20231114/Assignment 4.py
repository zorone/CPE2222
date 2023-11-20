import os
import platform

predefined = False
pf = 0

path = {
    "รายชื่อ": "รายชื่อพนักงานและนักศึกษา",
    "รายชื่อ/นักศึกษา": "รายชื่อนักศึกษาคณะวิศวกรรมศาสตร์",
    "รายชื่อ/อาจารย์": "รายชื่อคณาจารย์คณะวิศวกรรมศาสตร์",
    "รายชื่อ/อาจารย์/วิศวกรรมโยธา": "รายชื่อคณาจารย์สาขาวิศวกรรมโยธา",
    "รายชื่อ/อาจารย์/วิศวกรรมอุตสาหการ": "รายชื่อคณาจารย์สาขาวิศวกรรมอุตสาหการ",
    "รายชื่อ/อาจารย์/วิศวกรรมคอมพิวเตอร์": "รายชื่อคณาจารย์สาขาวิศวกรรมคอมพิวเตอร์"
}

if pf == 1:
    pf = "Windows"
else:
    pf = "Linux"

class Main():
    def __init__(self):
        try:
            self.baseCommand, self.trailing = platformSet()
            path = os.path.dirname(os.path.abspath(__file__))
            print(path)
            os.chdir(path)
            path = os.listdir()
            print(path)
            if "readme.txt" not in path:
                raise FileNotFoundError
            if "input.txt" not in path:
                raise FileNotFoundError
            
            name = list()
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
            
            for s in data:
                if not tempLock:
                    tempName = s
                    name += [tempName]
                    tempLock = True
                    continue
                
                if not tempSkip:
                    if len(nameType) > 1:
                        nameType.clear()
                        tempSkip = True
                        continue
                    if "นักศึกษา" in s:
                        student += [tempName]
                        tempSkip = True
                        continue
                    if "อาจารย์" in s:
                        instructor += [tempName]
                        nameType += ["instructor"]
                        continue
                    if "โยธา" in s:
                        CVE += [tempName]
                        nameType += ["CVE"]
                        continue
                    if "อุตสาหการ" in s:
                        IND += [tempName]
                        nameType += ["IND"]
                        continue
                    if "คอมพิวเตอร์" in s:
                        CPE += [tempName]
                        nameType += ["CPE"]
                        continue
                    
                if s == '\n':
                    tempLock = False
                    tempSkip = False

            F.close()
            
            self.fileGen()
            
        except FileNotFoundError:
            print("Incorrect file Structure, please check if your workspace has all files that is needed.")
            
        except FileExistsError:
            if self.trailing == '\\':
                os.system("rmdir /S .\รายชื่อ")
            else:
                os.system("rm -rf ./รายชื่อ")
            self.fileGen()
            
    def fileGen(self):
        key = path.keys()
        for k in key:
            os.mkdir(k)
            command = self.baseCommand + "./" + k + "/readme.txt"
            if self.trailing == '\\':
                command = command.replace('/', '\\')
            print(command)
            os.system(command)
        
def platformSet():
    plt = ''
    if predefined:
        plt = pf
    
    else:
        plt = platform.platform()
        
    print(plt)
    if plt == 'Windows':
        return "copy ./readme.txt ", '\\'
    else:
        return "cp ./readme.txt ", '/'

if __name__ == '__main__':
    main = Main()