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