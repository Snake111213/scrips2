''' Escriba una función que reciba un número y determine si es un número primo. 
El resultado que entrega la función será un valor lógico según corresponda. 
Junto a la función escriba un programa que liste los números primos existentes en un 
rango especificado
Solución
Si el programa se escribe junto con la función, primero debe escribirse la función y 
después el programa. En este caso, el programa no necesita importar la función 
que lo antecede.
Variables
n: número para probar si es primo
c: conteo de números divisores en la función
a,b: rango de búsqueda de número primos'''

#funcion primo
def primo(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c=c+1
    if c>2:
        return False
    else:
        return True

#Programa que lista primos en un rango
a=int(input('Desde: '))
b=int(input('Hasta: '))
for n in range(a,b+1):
    if primo(n):
        print('Numero primo: ',n)