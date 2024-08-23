import numpy as np

np.random.randint(0, 2, 16)
# array([1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0])

bits = np.random.randint(0, 2, 16)

enumerate(bits)
# <enumerate at 0x236cdac8440>
list(enumerate(bits))
'''
[(0, 1),
 (1, 0),
 (2, 1),
 (3, 0),
 (4, 0),
 (5, 1),
 (6, 1),
 (7, 0),
 (8, 0),
 (9, 0),
 (10, 0),
 (11, 1),
 (12, 1),
 (13, 1),
 (14, 1),
 (15, 1)]
'''

[i for i, bit in enumerate(bits)]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

[i for i, bit in enumerate(bits) if bit]
# [0, 2, 5, 6, 11, 12, 13, 14, 15]

bits
# array([1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1])

0 ^ 2 ^ 5 ^ 6 ^ 11 ^ 12 ^ 13 ^ 14 ^ 15
# 10

from functools import reduce
import operator as op

reduce(op.xor, [i for i, bit in enumerate(bits) if bit])
# 10

reduce(lambda x, y: x ^ y, [i for i, bit in enumerate(bits) if bit])
# 10

bin(10)
# '0b1010'

bits[2] = not bits[2]
bits[8] = not bits[8]

reduce(lambda x, y: x ^ y, [i for i, bit in enumerate(bits) if bit])
# 0

bits
# array([1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0])

bits[15] = not bits[15]
reduce(lambda x, y: x ^ y, [i for i, bit in enumerate(bits) if bit])
# 15

bits[15] = not bits[15]
reduce(lambda x, y: x ^ y, [i for i, bit in enumerate(bits) if bit])
# 0