from random import*
def laber(n,m):
    a=[]
    for i in range(n):
        f=[]
        for j in range(m):
            x=randint(0,1)
            f=f+[x]
        a=a+[f]
    for i in range(n):
        a[i][0]=1
        a[i][m-1]=1
    for j in range(m):
        a[0][j]=1
        a[n-1][j]=1
    return a

#prueba de la funcion laber
from numpy import*
a=laber(10,12)
b=array(a)
print(b)