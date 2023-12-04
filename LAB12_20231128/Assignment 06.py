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

Y = np.std(D.std(axis=2), axis=0)
Y = Y[:, np.newaxis]

A = D.sum(axis=(1,2))

J = (np.sum(((A*X)-Y))**2)
m = J.size
J = J/(2*m)

K = (np.sum(A*(X**2)-(Y*X)))
m = K.size
K = K/m

print('X[{},:] = {}'.format(0, X[0, :]))
print('X[{},:] = {}\n'.format(-1, X[-1, :]))
print('Y[{},0] = {}'.format(0, Y[0, 0]))
print('Y[{},0] = {}\n'.format(-1, Y[-1, 0]))
print("A = {}\n".format(A))

print(J)
print(K)