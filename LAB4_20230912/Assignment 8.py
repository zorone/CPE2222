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
char_amount = tuple()
char_ratio = tuple()

for i in range(-1, -5, -1):
    temp = point.index(s_point[i])
    char_point += (letter[temp], )
    point[temp] = -1
    
    temp = amount.index(s_amount[i])
    char_amount += (letter[temp], )
    amount[temp] = -1
    
    temp = ratio.index(s_ratio[(i*-1)-1])
    char_ratio += (letter[temp], )
    ratio[temp] = -1


print("The highest point in the scrabble game:")

for i in range(1, 5):
    print('        {}) "{}" with {} points'.format(i, char_point[i-1], s_point[i*-1]))

print("The highest amount in the scrabble game:")

for i in range(1, 5):
    print('        {}) "{}" with {} pieces'.format(i, char_amount[i-1], s_amount[i*-1]))

print("The lowest ratio in the scrabble game:")

for i in range(0, 4):
    print('        {}) "{}" with {} percent'.format(i+1, char_ratio[i], s_ratio[i]))