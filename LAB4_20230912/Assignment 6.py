testScore = {
                  "First": [20, 19, 10, 5],
                  "Second": [18, 20, 5, 3],
                  "Third": [19, 19, 4, 1]
                  }

dictionary = {"index": [0, 1, 2, 3],
              "Name": ["Peter", "Paul", "Mary", "Jenny"],
              "Age": [40, 25, 18, 60],
              "Gender": ["Male", "Male", "Female", "Female"],
              "Test": testScore
              }

print("\"{}\" is {}".format(dictionary["Name"][0], dictionary["Gender"][0]))

print("The 1st test score of \"{}\" is {}".format(dictionary["Name"][2], dictionary["Test"]["First"][2]))

print("The 2nd test score of \"{}\" is {}".format(dictionary["Name"][3], dictionary["Test"]["Second"][3]))

print("The 3rd test score of \"{}\" is {}".format(dictionary["Name"][1], dictionary["Test"]["Third"][1]))

dictionary["index"].append(4)
dictionary["Name"].append("Robert")
dictionary["Age"].append(35)
dictionary["Gender"].append("Male")
dictionary["Test"]["First"].append(10)
dictionary["Test"]["Second"].append(18)
dictionary["Test"]["Third"].append(5)

print("\"{}\" is {} years old".format(dictionary["Name"][4], dictionary["Age"][4]))

print("The dictionary to solve this problem was designed as: ")
print(dictionary)