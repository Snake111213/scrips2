from random import*
def randmat(n,m,a,b):
    c=[]
    for i in range(n):
        f=[]
        for j in range(m):
            x=randint(a,b)
            f=f+[x]
        c=c+[f]
    return c