import os
import numpy as np

path = os.path.dirname(os.path.abspath(__file__))
os.chdir(path)

_1 = np.loadtxt('1.csv')
_2 = np.loadtxt('2.csv')
_3 = np.loadtxt('3.csv')
_4 = np.loadtxt('4.csv')
_5 = np.loadtxt('5.csv')

D = np.array([_1, _2, _3, _4, _5])

X = np.transpose(D.mean(axis=1))
Y = D.std(axis=(0,1))

print('X[{},:] = {}'.format(0, X[0, :]))
print('X[{},:] = {}'.format(-1, X[-1, :]))
print(Y)