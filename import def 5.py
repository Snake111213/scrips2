#programa que lista primos en un rango
def primo(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c=c+1
        if c>2:
            return False
        else:
            return True

a=int(input('Desde: '))
b=int(input('Hasta: '))
for n in range(a,b+1):
    if primo(n):
        print('Numero primo: ',n)