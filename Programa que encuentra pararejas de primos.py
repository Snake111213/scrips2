def primo(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c=c+1

n=int(input('Ingrese un entero positivo: '))
for i in range(n):
    for j in range(n):
        if primo(i) and primo(j) and i+j==n:
            print('Pareja de primos: ',i,j)