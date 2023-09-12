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

s_point.sort(reverse=True)
s_amount.sort(reverse=True)
s_ratio.sort()

temp = int()

ch = tuple()
val = tuple()

for (i, search) in ((point, s_point), (amount, s_amount), (ratio, s_ratio)):
    for j in search[0:4]:
        temp = i.index(j)
        ch += (letter[temp], )
        val += (j, )
        i[temp] = -1


for (i, j, k) in (('highest', 'point', 'points'), ('highest', 'amount', 'pieces'), ('lowest', 'ratio', 'percent')):
    print("The {} {} in the scrabble game:".format(i, j))
    
    for c, v in {ch: val}:
        for n in range(1, 5):
            print('        {}) "{}" with {} {}'.format(n, c, v, k))
            