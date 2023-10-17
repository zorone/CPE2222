import module_exam as ext

studentID = ext.Info_Dict.keys()
availableSubject = ext.Info_Dict.values()
availableSubject = availableSubject.keys()

topic = str(input("Enter your subject {}".format(availableSubject)))

for ID in studentID:
    print(ID)