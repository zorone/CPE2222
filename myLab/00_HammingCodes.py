import numpy as np

np.random.randint(0, 2, 16)
# array([1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0])

bits = np.random.randint(0, 2, 16)

enumerate(bits)
# <enumerate at 0x1c2f9470700>

list(enumerate(bits))
'''
[(0, 1),
 (1, 1),
 (2, 0),
 (3, 0),
 (4, 0),
 (5, 1),
 (6, 0),
 (7, 0),
 (8, 1),
 (9, 1),
 (10, 0),
 (11, 0),
 (12, 1),
 (13, 0),
 (14, 1),
 (15, 0)]
'''

[i for i, bit in enumerate(bits)]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

[i for i, bit in enumerate(bits) if bit]
# [0, 1, 5, 8, 9, 12, 14]

bits
# array([1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0])

0 ^ 1 ^ 5 ^ 8 ^ 9 ^ 12 ^ 14
# 7

from functools import reduce
import operator as op

reduce(op.xor, [i for i, bit in enumerate(bits) if bit])
# 7

reduce(lambda x, y: x ^ y, [i for i, bit in enumerate(bits) if bit])
# 7

bin(7)
# '0b111'

bits[8] = not bits[8]
bits[1] = not bits[1]

reduce(lambda x, y: x ^ y, [i for i, bit in enumerate(bits) if bit])
# 14

bits
# array([1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0])

bits[10] = not bits[10]
reduce(lambda x, y: x ^ y, [i for i, bit in enumerate(bits) if bit])
# 4

bits[10] = not bits[10]
reduce(lambda x, y: x ^ y, [i for i, bit in enumerate(bits) if bit])
# 14

_ih
'''
['',
 'import numpy as np',
 'np.random.randint(0, 2, 16)',
 'bits = np.random.randint(0, 2, 16)',
 'enumerate(bits)',
 'list(enumerate(bits))',
 '[i for i, bit in enumerate(bits)]',
 '[i for i, bit in enumerate(bits) if bit]',
 'bits',
 '0 ^ 1 ^ 5 ^ 8 ^ 9 ^ 12 ^ 14',
 'from functools import reduce',
 'import operator as op',
 'reduce(op.xor, [i for i, bit in enumerate(bits) if bit])',
 'reduce(lambda x, y: x ^ y, [i for i, bit in enumerate(bits) if bit])',
 'bin(7)',
 'bits[8] = not bits[8]',
 'bits[1] = not bits[1]',
 'reduce(lambda x, y: x ^ y, [i for i, bit in enumerate(bits) if bit])',
 'bits',
 'bits[10] = not bits[10]',
 'reduce(lambda x, y: x ^ y, [i for i, bit in enumerate(bits) if bit])',
 'bits[10] = not bits[10]',
 'reduce(lambda x, y: x ^ y, [i for i, bit in enumerate(bits) if bit])',
 '_ih']
'''