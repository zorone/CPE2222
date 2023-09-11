scrabble = ['a',1,9,4.8,'b',3,2,3.2,'c',3,2,3.2,'d',2,4,4.3,'e',1,12,6.4,'f',4,2,4.3,'g',2,3,3.2,'h',4,2,4.3,
            'i',1,9,4.8,'j',8,1,4.3,'k',5,1,2.7,'l',1,4,2.1,'m',3,2,3.2,'n',1,6,3.2,'o',1,8,4.3,'p',3,2,3.2,
            'q',10,1,5.3,'r',1,6,3.2,'s',1,4,2.1,'t',1,6,3.2,'u',1,4,2.1,'v',4,2,4.3,'w',4,2,4.3,'x',8,1,4.3,
            'y',4,2,4.3,'z',10,1,5.3]

letter = scrabble[0::4]
point = scrabble[1::4]
amount = scrabble[2::4]
ratio = scrabble[3::4]

s_point = point.sort()
s_amount = amount.sort()
s_ratio = ratio.sort()

char_point = tuple()
char_point += (letter[point.index(s_point[-1])], )
char_point += (letter[point.index(s_point[-2])], )
char_point += (letter[point.index(s_point[-3])], )
char_point += (letter[point.index(s_point[-4])], )

char_amount = tuple()
char_amount += (letter[amount.index(s_amount[-1])], )
char_amount += (letter[amount.index(s_amount[-2])], )
char_amount += (letter[amount.index(s_amount[-3])], )
char_amount += (letter[amount.index(s_amount[-4])], )

char_ratio = tuple()

print("The highest point in the scrabble game:")
print('        1) "{}" with {} points'.format())