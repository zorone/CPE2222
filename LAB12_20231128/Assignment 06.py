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
A = A.reshape(1, 5)

J1 = np.matmul(A, np.transpose(X))-np.transpose(Y)
J2 = J1.sum()
J = J2**2/(2*J1.size)

K1 = X**2
K2 = np.matmul(A, np.transpose(K1))
K3 = np.sum(K2)
K4 = np.matmul(np.transpose(Y), X)
K5 = K3-K4
K = K5/K2.size

print('X[{},:] = {}'.format(0, X[0, :]))
print('X[{},:] = {}\n'.format(-1, X[-1, :]))
print('Y[{},0] = {}'.format(0, Y[0, 0]))
print('Y[{},0] = {}\n'.format(-1, Y[-1, 0]))
print("A = {}\n".format(A))
print("J = {}\n".format(J))
print("K = {}\n".format(K))
