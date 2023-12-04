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

print('X[{},:] = {}'.format(0, X[0, :]))
print('X[{},:] = {}\n'.format(-1, X[-1, :]))
print('Y[{},0] = {}'.format(0, Y[0, 0]))
print('Y[{},0] = {}\n'.format(-1, Y[-1, 0]))
print("A = {}\n".format(A))

J = np.sum((A*X-Y)**2)/(40)
print(J)

J = (np.sum(A*X-Y)**2)/(20000)
print(J)

K = (np.sum(A*(X**2)-(Y*X), axis=0)/20)
print(K)

K = np.mean((np.sum(A*(X**2), axis=0)-(Y*X)), axis=0)/20
print(K)

K = (np.mean(A*(X**2)-(Y*X), axis=0))*5
print(K)

for i in range(0, 2):
    for j in range(0, 2):
        if i == 0 and j == 0: continue
        if i == 0 and j == 1: continue
        if i == 1 and j == 0: continue
        K = (np.sum(A*(X**2), axis=i) - np.sum(Y*X, axis=j))/20
        print(K)

for i in range(0, 2):
    for j in range(0, 2):
        if i == 0 and j == 0: continue
        K = np.sum(np.sum(A*(X**2), axis=i)-(Y*X), axis=j)
        print(K)

for i in range(0, 2):
    K = np.sum(A*(X**2)-(Y*X), axis=i)
    print(K)