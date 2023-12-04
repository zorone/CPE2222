import os
import numpy as np

path = os.path.dirname(os.path.abspath(__file__))
os.chdir(path)

_1 = np.loadtxt('1.csv')
_2 = np.loadtxt('2.csv')
_3 = np.loadtxt('3.csv')
_4 = np.loadtxt('4.csv')
_5 = np.loadtxt('5.csv')

D = _1
np.concatenate(D, _2)
np.concatenate(D, _3)
np.concatenate(D, _4)
np.concatenate(D, _5)

print(D)