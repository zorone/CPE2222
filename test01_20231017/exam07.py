import module_exam as ext

studentID = ext.Info_Dict.keys()

for ID in studentID:
    availableSubject = ext.Info_Dict[ID].keys()

topic = str(input("Enter your subject {}".format(availableSubject)))