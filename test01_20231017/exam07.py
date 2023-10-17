import module_exam as ext

studentID = ext.Info_Dict.keys()

for ID in studentID:
    availableSubject = ext.Info_Dict[ID].keys()
    break;

inputPrompt = "Enter your subject ["
for subject in availableSubject:
    inputPrompt += subject;
    inputPrompt += ", ";

inputPrompt.rstrip()
inputPrompt = inputPrompt[0:len(inputPrompt)-2]
inputPrompt += "]:"

topic = str(input(inputPrompt))

pageBreak = "-"*50

print(pageBreak)

if topic not in subject:
    print("!!!  Subject Error !!!")
else:
    stat = {"A": [0, 0],
            "B+": [0, 0],
            "B": [0, 0],
            "C+": [0, 0],
            "C": [0, 0],
            "D+": [0, 0],
            "D": [0, 0],
            "F": [0, 0]}
    for student in ext.Info_Dict:
        tempScore = student[topic]
        print(tempScore)

print(pageBreak)