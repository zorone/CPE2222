import numpy as np

np.random.randint(0, 2, 16)
# array([1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1])

bits = np.random.randint(0, 2, 16)

enumerate(bits)
# <enumerate at 0x25452421100>
list(enumerate(bits))
'''
[(0, 1),
 (1, 0),
 (2, 1),
 (3, 0),
 (4, 0),
 (5, 1),
 (6, 0),
 (7, 1),
 (8, 0),
 (9, 1),
 (10, 0),
 (11, 1),
 (12, 0),
 (13, 1),
 (14, 1),
 (15, 0)]
'''

[i for i, bit in enumerate(bits)]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

[i for i, bit in enumerate(bits) if bit]
# [0, 2, 5, 7, 9, 11, 13, 14]

bits
# array([1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0])

0 ^ 2 ^ 5 ^ 7 ^ 9 ^ 11 ^ 13 ^ 14
# 1

from functools import reduce
import operator as op

reduce(op.xor, [i for i, bit in enumerate(bits) if bit])
# 1

reduce(lambda x, y: x ^ y, [i for i, bit in enumerate(bits) if bit])
# 1

bin(1)
# '0b1'

bits[1] = not bits[1]

reduce(lambda x, y: x ^ y, [i for i, bit in enumerate(bits) if bit])
# 0

bits
# array([1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0])

bits[10] = not bits[10]
reduce(lambda x, y: x ^ y, [i for i, bit in enumerate(bits) if bit])
# 10

bits[10] = not bits[10]
reduce(lambda x, y: x ^ y, [i for i, bit in enumerate(bits) if bit])
# 0