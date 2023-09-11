scrabble = ['a',1,9,4.8,'b',3,2,3.2,'c',3,2,3.2,'d',2,4,4.3,'e',1,12,6.4,'f',4,2,4.3,'g',2,3,3.2,'h',4,2,4.3,
            'i',1,9,4.8,'j',8,1,4.3,'k',5,1,2.7,'l',1,4,2.1,'m',3,2,3.2,'n',1,6,3.2,'o',1,8,4.3,'p',3,2,3.2,
            'q',10,1,5.3,'r',1,6,3.2,'s',1,4,2.1,'t',1,6,3.2,'u',1,4,2.1,'v',4,2,4.3,'w',4,2,4.3,'x',8,1,4.3,
            'y',4,2,4.3,'z',10,1,5.3]

letter = scrabble[0::4]
point = scrabble[1::4]
amount = scrabble[2::4]
ratio = scrabble[3::4]

s_point = point.copy()
s_amount = amount.copy()
s_ratio = ratio.copy()

s_point.sort()
s_amount.sort()
s_ratio.sort()

temp = int()

char_point = tuple()
temp = point.index(s_point[-1])
char_point += (letter[temp], )
point[temp] = -1
temp = point.index(s_point[-2])
char_point += (letter[temp], )
point[temp] = -1
temp = point.index(s_point[-3])
char_point += (letter[temp], )
point[temp] = -1
temp = point.index(s_point[-4])
char_point += (letter[temp], )
point[temp] = -1

char_amount = tuple()
temp = amount.index(s_amount[-1])
char_amount += (letter[temp], )
amount[temp] = -1
temp = amount.index(s_amount[-2])
char_amount += (letter[temp], )
amount[temp] = -1
temp = amount.index(s_amount[-3])
char_amount += (letter[temp], )
amount[temp] = -1
temp = amount.index(s_amount[-4])
char_amount += (letter[temp], )
amount[temp] = -1

char_ratio = tuple()
temp = ratio.index(s_ratio[0])
char_ratio += (letter[temp], )
ratio[temp] = -1
temp = ratio.index(s_ratio[1])
char_ratio += (letter[temp], )
ratio[temp] = -1
temp = ratio.index(s_ratio[2])
char_ratio += (letter[temp], )
ratio[temp] = -1
temp = ratio.index(s_ratio[3])
char_ratio += (letter[temp], )
ratio[temp] = -1

print("The highest point in the scrabble game:")
print('        1) "{}" with {} points'.format(char_point[0], s_point[-1]))
print('        2) "{}" with {} points'.format(char_point[1], s_point[-2]))
print('        3) "{}" with {} points'.format(char_point[2], s_point[-3]))
print('        4) "{}" with {} points'.format(char_point[3], s_point[-4]))

print("The highest amount in the scrabble game:")
print('        1) "{}" with {} pieces'.format(char_amount[0], s_amount[-1]))
print('        2) "{}" with {} pieces'.format(char_amount[1], s_amount[-2]))
print('        3) "{}" with {} pieces'.format(char_amount[2], s_amount[-3]))
print('        4) "{}" with {} pieces'.format(char_amount[3], s_amount[-4]))

print("The lowest ratio in the scrabble game:")
print('        1) "{}" with {} percent'.format(char_ratio[0], s_ratio[0]))
print('        2) "{}" with {} percent'.format(char_ratio[1], s_ratio[1]))
print('        3) "{}" with {} percent'.format(char_ratio[2], s_ratio[2]))
print('        4) "{}" with {} percent'.format(char_ratio[3], s_ratio[3]))