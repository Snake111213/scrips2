from numpy import *
def matbuscar(a,x):
    [n,m]=shape(a)
    for i in range(n):
        for j in range(n):
            if x==a[i][j]:
                return [i,j]
        return [-1,-1]
