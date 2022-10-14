def rango_doble(n,m):
    for i in range(1,n):
        for j in range(1,m):
            for j in range(1,m):
                yield [i,j]

for i,j in rango_doble(10,10):
    n = 2*i**3+3*j**2
    if n%7==0:
        print(i,j,n)
        break
    