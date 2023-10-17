import module_exam as ext

studentID = ext.Info_Dict.keys()

for ID in studentID:
    availableSubject = ext.Info_Dict[ID].keys()
    break;

inputPrompt = "Enter your subject ["
for subject in availableSubject:
    inputPrompt += subject
    inputPrompt += ", "

inputPrompt.rstrip()
inputPrompt = inputPrompt[0:len(inputPrompt)-2]
inputPrompt += "]:"

topic = str(input(inputPrompt))

pageBreak = "-"*50

print(pageBreak)

if topic not in subject:
    print("!!!  Subject Error !!!")
else:
    textCol1 = "Grade"
    textCol2 = "A number of students (Percentage) "
    print("{}{}".format(textCol1.center(7), textCol2.rjust(43)))
    stat = {"A": [0, 0],
            "B+": [0, 0],
            "B": [0, 0],
            "C+": [0, 0],
            "C": [0, 0],
            "D+": [0, 0],
            "D": [0, 0],
            "F": [0, 0]}
    
    sum = 0
    average = 0
    grade = str()
    count = 0
    for student in studentID:
        tempScore = ext.Info_Dict[student][topic]
        sum += tempScore
        count += 1
        grade = ext.grading(topic, tempScore)
        stat[grade][0] += 1
    
    for grade in stat.keys():
        stat[grade][1] = stat[grade][0] / count
        text = print("{} ({})".format(stat[grade][0], stat[grade][1]))
        print("{}{}".format(grade.center(7), text.center(43)))

    average = sum/count
    print(pageBreak)
    print("   Average Score = {}".format(average))

print(pageBreak)