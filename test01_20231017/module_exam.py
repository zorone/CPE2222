Info_Dict = {'66001': {'Mathematics': 18, 'Physics': 44, 'English': 16, 'Chemistry': 30, 'Computer': 83},
             '66002': {'Mathematics': 58, 'Physics': 47, 'English': 79, 'Chemistry': 90, 'Computer': 95},
             '66003': {'Mathematics': 58, 'Physics': 80, 'English': 70, 'Chemistry': 91, 'Computer': 93},
             '66004': {'Mathematics': 98, 'Physics': 52, 'English': 96, 'Chemistry': 55, 'Computer': 72},
             '66005': {'Mathematics': 22, 'Physics': 26, 'English': 6, 'Chemistry': 98, 'Computer': 45},
             '66006': {'Mathematics': 90, 'Physics': 51, 'English': 77, 'Chemistry': 65, 'Computer': 42},
             '66007': {'Mathematics': 50, 'Physics': 59, 'English': 31, 'Chemistry': 63, 'Computer': 58},
             '66008': {'Mathematics': 93, 'Physics': 71, 'English': 91, 'Chemistry': 74, 'Computer': 1},
             '66009': {'Mathematics': 44, 'Physics': 35, 'English': 79, 'Chemistry': 32, 'Computer': 88},
             '66010': {'Mathematics': 55, 'Physics': 48, 'English': 99, 'Chemistry': 18, 'Computer': 14},
             '66011': {'Mathematics': 64, 'Physics': 20, 'English': 64, 'Chemistry': 7, 'Computer': 60},
             '66012': {'Mathematics': 14, 'Physics': 83, 'English': 91, 'Chemistry': 86, 'Computer': 24},
             '66013': {'Mathematics': 68, 'Physics': 81, 'English': 37, 'Chemistry': 74, 'Computer': 67},
             '66014': {'Mathematics': 15, 'Physics': 15, 'English': 88, 'Chemistry': 41, 'Computer': 15},
             '66015': {'Mathematics': 10, 'Physics': 23, 'English': 75, 'Chemistry': 21, 'Computer': 92},
             '66016': {'Mathematics': 94, 'Physics': 0, 'English': 43, 'Chemistry': 6, 'Computer': 76},
             '66017': {'Mathematics': 58, 'Physics': 77, 'English': 67, 'Chemistry': 96, 'Computer': 26},
             '66018': {'Mathematics': 33, 'Physics': 50, 'English': 87, 'Chemistry': 35, 'Computer': 5},
             '66019': {'Mathematics': 6, 'Physics': 18, 'English': 43, 'Chemistry': 90, 'Computer': 49},
             '66020': {'Mathematics': 84, 'Physics': 99, 'English': 69, 'Chemistry': 89, 'Computer': 92},
             '66021': {'Mathematics': 82, 'Physics': 72, 'English': 46, 'Chemistry': 15, 'Computer': 13},
             '66022': {'Mathematics': 26, 'Physics': 20, 'English': 61, 'Chemistry': 91, 'Computer': 51},
             '66023': {'Mathematics': 42, 'Physics': 24, 'English': 51, 'Chemistry': 6, 'Computer': 86},
             '66024': {'Mathematics': 29, 'Physics': 21, 'English': 97, 'Chemistry': 100, 'Computer': 91},
             '66025': {'Mathematics': 39, 'Physics': 3, 'English': 7, 'Chemistry': 76, 'Computer': 19},
             '66026': {'Mathematics': 98, 'Physics': 85, 'English': 12, 'Chemistry': 28, 'Computer': 79},
             '66027': {'Mathematics': 26, 'Physics': 30, 'English': 38, 'Chemistry': 39, 'Computer': 84},
             '66028': {'Mathematics': 22, 'Physics': 57, 'English': 83, 'Chemistry': 67, 'Computer': 82},
             '66029': {'Mathematics': 18, 'Physics': 81, 'English': 55, 'Chemistry': 79, 'Computer': 61},
             '66030': {'Mathematics': 24, 'Physics': 49, 'English': 32, 'Chemistry': 27, 'Computer': 69}
}

def grading(subject,score):
    SUBJECTs = ['Mathematics','Physics','English','Chemistry','Computer']
    if subject not in SUBJECTs:
        print('!!!Subject is error!!!')
        exit()
    Info_Dict = {'Mathematics': {'A':85,'B+':80,'B':75,'C+':65,'C':50,'D+':45,'D':40},
                 'Physics': {'A':85,'B+':78,'B':72,'C+':64,'C':52,'D+':48,'D':35},
                 'English': {'A':80,'B+':75,'B':70,'C+':65,'C':60,'D+':55,'D':50},
                 'Chemistry': {'A':82,'B+':79,'B':72,'C+':63,'C':57,'D+':52,'D':45},
                 'Computer': {'A':90,'B+':85,'B':80,'C+':70,'C':60,'D+':50,'D':40}
    }
    if score > Info_Dict[subject]['A']: return('A')
    elif score > Info_Dict[subject]['B+']: return('B+')
    elif score > Info_Dict[subject]['B']: return('B')
    elif score > Info_Dict[subject]['C+']: return('C+')
    elif score > Info_Dict[subject]['C']: return('C')
    elif score > Info_Dict[subject]['D+']: return('D+')
    elif score > Info_Dict[subject]['D']: return('D')
    else: return('F')
